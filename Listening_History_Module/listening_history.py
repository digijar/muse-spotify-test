# all imports
from flask import Flask, request, jsonify, session
from flask_cors import CORS
import os
from os import environ
import requests
from invokes import invoke_http
import amqp_setup
import pika
import json
import pymongo
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)
app.secret_key = os.urandom(24)

### URLs to call
notifications_URL = environ.get('notifications_URL') or "http://127.0.0.1:4999/api/v1/top_items_email"
error_URL = environ.get('error_URL') or "http://127.0.0.1:4997/api/v1/error"

# for API Keys
from dotenv import load_dotenv
load_dotenv('spotify_api_keys.env')
user = os.getenv('user')
password = os.getenv('password')
SPOTIFY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
SPOTIFY_CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')
SPOTIFY_REDIRECT_URI = os.getenv('SPOTIFY_REDIRECT_URI')
SPOTIFY_AUTH_URL = 'https://accounts.spotify.com/authorize'
SPOTIFY_TOKEN_URL = 'https://accounts.spotify.com/api/token'

### Connecting to MongoDB
mongo_uri = f"mongodb+srv://{user}:{password}@musecluster.egcmgf4.mongodb.net/?retryWrites=true&w=majority"

# Create a MongoDB client and connect to the sample_training database
client = MongoClient(mongo_uri, ssl=True, tlsAllowInvalidCertificates=True)
db = client.ESD_Muse


@app.route("/api/v1/get_top_tracks")
def get_top_tracks():
    email = request.headers.get('Email', '')
    data = {
        'Email': email,
    }
    top_tracks_info = requests.get('http://replay:5001/replay/get_top_tracks', params=data).json()
    print(top_tracks_info)
    return jsonify(top_tracks_info)

@app.route("/api/v1/get_top_artists")
def get_top_artists():
    email = request.headers.get('Email', '')
    data = {
        'Email': email,
    }
    top_artists_info = requests.get('http://replay:5001/replay/get_top_artists', params=data).json()
    print(top_artists_info)
    return jsonify(top_artists_info)

@app.route("/api/v1/reload_top_items")
def reload_top_items():
    access_token = request.headers.get('Authorization', '').replace('Bearer ', '')
    email = request.headers.get('Email', '')
    data = {
        'Email': email,
        'access_token': access_token
    }

    # call reload function
    reload_info = requests.get('http://replay:5001/replay/reload_top_items', params=data).json()
    print(reload_info)

    # create top_artists array
    top_artist_arr = []
    for artist in get_top_artists().json["items"]:
        top_artist_arr.append(artist["name"])

    # create top_tracks array
    top_tracks_arr = []
    for track in get_top_tracks().json["items"]:
        top_tracks_arr.append(track["name"])

    if reload_info["code"] == 200:
        data = {"email": email, "top_artists": top_artist_arr, "top_tracks": top_tracks_arr}
        top_items_json = json.dumps(data)

        print('\n\n-----Publishing the top items email with routing_key=top.notification-----')
        amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key="top.notification", 
        body=top_items_json, properties=pika.BasicProperties(delivery_mode = 2))

        # send top items to notification microservice
        result = processEmail(top_items_json)
        print('\n------------------------')
        print('\nresult: ', result)

    else:
        # error handling
        error_payload = {
            "code": 500,
            "message": "An error occurred while reloading top items of user"
        }
        message = json.dumps(error_payload)
        print('\n\n-----Publishing the (notification error) message with routing_key=top.error-----')

        amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key="top.error", 
            body=message, properties=pika.BasicProperties(delivery_mode = 2)) 
        
        error_result = invoke_http(error_URL, method='POST', json=error_payload)
        print('error_result:', error_result)

        return {
            "code": 500,
            "message": "Notification failure sent for error handling."
        }

    return jsonify(reload_info)

def processEmail(top_items_json):
    # Invoke the notification microservice
    print('\n-----Invoking notification microservice-----')
    notification_result = invoke_http(notifications_URL, method='POST', json=top_items_json)
    print('notification_result:', notification_result)

    code = notification_result["code"]
    message = json.dumps(notification_result)

    error_payload = {
        "code": notification_result["code"],
        "message": notification_result["message"]
    }

    amqp_setup.check_setup()

    if code not in range(200, 300):
        # Inform the error microservice
        print('\n\n-----Publishing the (notification error) message with routing_key=notification.error-----')

        amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key="notification.error", 
            body=message, properties=pika.BasicProperties(delivery_mode = 2)) 
        
        error_result = invoke_http(error_URL, method='POST', json=error_payload)
        print('error_result:', error_result)

        return {
            "code": 500,
            "data": {"notification_result": notification_result},
            "message": "Notification failure sent for error handling."
        }
    
    print("\nTop Items published to RabbitMQ Exchange.\n")

    return {
        "code": 201,
        "data": {
            "notification_result": notification_result,
        }
    }


if __name__ == "__main__":
    print("This is flask " + os.path.basename(__file__) + " for the 'Listening History' complex microservice...")
    app.run(host="0.0.0.0", port=5005, debug=True)