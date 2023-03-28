# all imports
from flask import Flask, request, jsonify, session
from flask_cors import CORS
import os, sys
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

# authentication_URL = "http://127.0.0.1:5002"
# replay_URL = "http://127.0.0.1:5001"
recommendations_URL = "http://127.0.0.1:5000"
notifications_URL = "http://127.0.0.1:4999/api/v1/email"
error_URL = "http://127.0.0.1:4997/api/v1/error"

# for API Keys
from dotenv import load_dotenv
load_dotenv('spotify_api_keys.env')

username = os.getenv('username')
password = os.getenv('password')
SPOTIFY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
SPOTIFY_CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')
SPOTIFY_REDIRECT_URI = os.getenv('SPOTIFY_REDIRECT_URI')
SPOTIFY_AUTH_URL = 'https://accounts.spotify.com/authorize'
SPOTIFY_TOKEN_URL = 'https://accounts.spotify.com/api/token'

### Connecting to MongoDB
mongo_uri = f"mongodb+srv://{username}:{password}@musecluster.egcmgf4.mongodb.net/?retryWrites=true&w=majority"

# Create a MongoDB client and connect to the sample_training database
client = MongoClient(mongo_uri, ssl=True, tlsAllowInvalidCertificates=True)
db = client.ESD_Muse

# for PlaylistCard component on BlendPage component which is on GroupBlendView
@app.route("/api/v1/get_groups")
def get_groups():
    email = request.headers.get('Email', '')
    group_names = []
    for result in db.group.find({}):
        if email in result["friends"]:
            group_names.append(result["group_name"])

    return jsonify(group_names)

# for InviteFriend component on BlendView
@app.route("/api/v1/get_friends")
def get_friends():
    email = request.headers.get('Email', '')
    group_name = request.headers.get('group_name', '')

    friend_names = []
    for result in db.group.find({"group_name": group_name}):
        for name in result["friends"]:
            if name != email:
                friend_names.append(name)

    return jsonify(friend_names)

# send friend email notification + add friend into group
@app.route("/api/v1/add_friend", methods=['POST'])
def add_friend():
    data = request.json
    friend_email = data.get('friend_email')
    group_name = data.get('group_name')

    # Check if the group exists in the database
    group = db.group.find_one({'group_name': group_name})
    if group is None:
        return jsonify({'message': 'Group not found'}), 404

    friends = group.get('friends', [])

    # Check if the friend is already in the group
    if friend_email in friends:
        return jsonify({'message': 'Friend is already in the group'}), 404

    # If friend not in group,
    # Add the friend to the group
    friends.append(friend_email)
    result = db.group.update_one({'group_name': group_name}, {'$set': {'friends': friends}})

    # convert friend's email to json
    data = {"friend_email": friend_email}
    friend_json = json.dumps(data)

    # sending friend's email to notification queue
    print('\n\n-----Publishing the friends email with routing_key=friend.notification-----')

    amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key="friend.notification", 
        body=friend_json, properties=pika.BasicProperties(delivery_mode = 2)) 

    # send friend_email to notification microservice
    result = processEmail(friend_json)
    print('\n------------------------')
    print('\nresult: ', result)

    return jsonify({'message': 'Friend added successfully'}), 201


def processEmail(friend_json):
    # Invoke the notification microservice
    print('\n-----Invoking notification microservice-----')
    notification_result = invoke_http(notifications_URL, method='POST', json=friend_json)
    print('notification_result:', notification_result)

    code = notification_result["code"]
    message = json.dumps(notification_result)

    amqp_setup.check_setup()

    if code not in range(200, 300):
        # Inform the error microservice
        print('\n\n-----Publishing the (notification error) message with routing_key=notification.error-----')

        amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key="notification.error", 
            body=message, properties=pika.BasicProperties(delivery_mode = 2)) 
        
        error_result = invoke_http(error_URL, method='POST', json=message)
        print('error_result:', error_result)

        return {
            "code": 500,
            "data": {"notification_result": notification_result},
            "message": "Notification failure sent for error handling."
        }
    
    print("\nFriend's Email published to RabbitMQ Exchange.\n")

    return {
        "code": 201,
        "data": {
            "notification_result": notification_result,
        }
    }


if __name__ == "__main__":
    print("This is flask " + os.path.basename(__file__) + " for the group complex microservice...")
    app.run(host="0.0.0.0", port=4998, debug=True)
