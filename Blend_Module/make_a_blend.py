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
import re

app = Flask(__name__)
CORS(app)
app.secret_key = os.urandom(24)

### URLs to call
recommendations_URL = "http://127.0.0.1:5000/generate_recommendations"
notifications_URL = "http://127.0.0.1:4999/api/v1/email"
error_URL = "http://127.0.0.1:4997/api/v1/error"

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

### add_friend (has to be here since invokes notification and error) ###
################ for notification and error microservice ###################
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


### get_recommendations (invokes recommendation) ###
@app.route("/api/v1/get_recommendations")
def get_recommendations():
    access_token = request.headers.get('Authorization', '').replace('Bearer ', '')
    email = request.headers.get('Email', '')
    group_name = request.headers.get('group_name', '')
    playlist_ids = request.headers.get('playlist_ids')
    
    params = {
        "access_token": access_token,
        "playlist_ids": playlist_ids
    }
    headers = {
        "access_token": access_token,
        "playlist_ids": playlist_ids,
        'Content-Type': 'application/json',
        'Authorization': f"Bearer {access_token}"
    }

    # Make the request to the Recommendations Microservice API endpoint
    response = requests.post(recommendations_URL, headers=headers).json()

    if response["code"] == 201:
        recommended_playlist_id = response["id"]

        playlist_info = requests.get(f'https://api.spotify.com/v1/playlists/{recommended_playlist_id}', headers=headers).json()

        result = db.group.update_one(
            {'group_name': group_name, "recommended_playlist": { "$exists": True }},
            {"$set": {"recommended_playlist": playlist_info}},
        )

        # if no documents are updated, add a new recommend_playlist field
        if result.modified_count == 0:
            update_new = {"$set": {"recommended_playlist": playlist_info}}
            result = db.group.update_one({"group_name": group_name}, update_new)

        print("recommended playlist added into mongoDB")
        return jsonify({"code": 201, "message": "recommended playlist successfully created"})
    
    print("error creating recommended playlist")
    return jsonify({"code": 500, "message": "recommended playlist creation not successful"})

### requests get_groups ###
@app.route("/api/v1/get_groups")
def get_groups():
    email = request.headers.get('Email', '')
    data = {
        'Email': email,
    }
    group_info = requests.get(f'http://127.0.0.1:4998/group/get_groups', json=data).json()
    return jsonify(group_info)

### requests get_friends ###
@app.route("/api/v1/get_friends")
def get_friends():
    email = request.headers.get('Email', '')
    group_name = request.headers.get('group_name', '')
    data = {
        'Email': email,
        'group_name': group_name
    }
    friends_info = requests.get(f'http://127.0.0.1:4998/group/get_friends', json=data).json()
    return jsonify(friends_info)

### requests check_personalUpload ###
@app.route("/api/v1/check_personalUpload")
def check_personalUpload():
    access_token = request.headers.get('Authorization', '').replace('Bearer ', '')
    email = request.headers.get('Email', '')
    group_name = request.headers.get('group_name', '')
    data = {
        'access_token': access_token,
        'email': email,
        'group_name': group_name
    }
    personal_upload_info = requests.get(f'http://127.0.0.1:4998/group/check_personalUpload', json=data).json()
    return jsonify(personal_upload_info)

### requests check_groupStatus ### 
@app.route("/api/v1/check_groupStatus")
def check_groupStatus():
    group_name = request.headers.get('group_name', '')
    data = {
        'group_name': group_name
    }
    group_status_info = requests.get(f'http://127.0.0.1:4998/group/check_groupStatus', json=data).json()
    return jsonify(group_status_info)

### requests check_recommendedStatus ### 
@app.route("/api/v1/check_recommendedStatus")
def check_recommendedStatus():
    group_name = request.headers.get('group_name', '')
    data = {
        'group_name': group_name
    }
    recommended_status_info = requests.get(f'http://127.0.0.1:4998/group/check_recommendedStatus', json=data).json()
    return jsonify(recommended_status_info)

### requests save_playlist (post) ###
@app.route("/api/v1/save_playlist")
def save_playlist():
    data = request.get_json()
    playlist_link = data.get('playlist_link')
    email = data.get('email')
    group_name = request.headers.get('group_name', '')
    playlist_id = re.search(r'playlist\/(\w+)', playlist_link).group(1)
    data = {
        'Email': email,
        'group_name': group_name,
        'playlist_id': playlist_id
    }
    save_playlist_info = requests.post(f'http://127.0.0.1:4998/group/save_playlist', json=data).json()
    return jsonify(save_playlist_info)

### requests create_group (post) ###
@app.route("/api/v1/create_group")
def create_group():
    data = request.json
    email = data.get('email')
    group_name = data.get('group_name')
    data = {
        'Email': email,
        'group_name': group_name
    }
    group_creation_info = requests.post(f'http://127.0.0.1:4998/group/create_group', json=data).json()
    return jsonify(group_creation_info)


### technical function remove playlist ###
@app.route("/api/v1/remove_playlist")
def remove_playlist():
    group_name = request.headers.get('group_name', '')
    data = {
        'group_name': group_name
    }
    playlist_deletion_info = requests.post(f'http://127.0.0.1:4998/group/remove_playlist', json=data).json()
    return jsonify(playlist_deletion_info)


if __name__ == "__main__":
    print("This is flask " + os.path.basename(__file__) + " for the 'Make a Blend' complex microservice...")
    app.run(host="0.0.0.0", port=5004, debug=True)