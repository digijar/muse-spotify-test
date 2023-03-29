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

# authentication_URL = "http://127.0.0.1:5002"
# replay_URL = "http://127.0.0.1:5001"
recommendations_URL = "http://127.0.0.1:5000/generate_recommendations"
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




############ for recommendations microservice ##############
@app.route("/api/v1/check_personalUpload")
def check_personalUpload():
    access_token = request.headers.get('Authorization', '').replace('Bearer ', '')
    email = request.headers.get('Email', '')
    group_name = request.headers.get('group_name', '')

    personalUpload = False
    playlistID = ""
    for result in db.group.find({"group_name": group_name, "user_and_playlist": { "$exists": True }}):
        if len(result["user_and_playlist"]) > 1:
            for emails in result["user_and_playlist"]:
                if email == emails["email"]:
                    personalUpload = True
                    playlistID = emails["playlistID"]

    ## get uploaded playlist details
    if personalUpload == True and playlistID != "":
        headers = {
            'Authorization': f"Bearer {access_token}"
        }

        playlist_response = requests.get(f'https://api.spotify.com/v1/playlists/{playlistID}', headers=headers)

        if playlist_response.status_code != 200:
            print("Error getting playlist:", playlist_response.status_code, playlist_response.text)
            return jsonify({"code": 500, "bool": False, "message": "An error occurred while getting playlist."})
        else:
            playlist_data = playlist_response.json()
            return jsonify({"code": 200, "bool": personalUpload, "name": playlist_data["name"], "link": playlist_data["external_urls"]["spotify"], "cover": playlist_data["images"][0]["url"]})
    else:
        return jsonify({"bool": personalUpload})

@app.route("/api/v1/check_groupStatus")
def check_groupStatus():
    email = request.headers.get('Email', '')
    group_name = request.headers.get('group_name', '')

    groupStatus = False
    user_and_playlist_arr = []

    for result in db.group.find({"group_name": group_name, "user_and_playlist": { "$exists": True }}):
        if len(result["user_and_playlist"]) == len(result["friends"]):
            groupStatus = True
            for arr in result["user_and_playlist"]:
                user_and_playlist_arr.append(arr["playlistID"])

    return jsonify({"bool": groupStatus, "playlist_arr": user_and_playlist_arr})

@app.route("/api/v1/check_recommendedStatus")
def check_recommendedStatus():
    email = request.headers.get('Email', '')
    group_name = request.headers.get('group_name', '')

    recommendedStatus = False
    recommended_playlist = {}
    for result in db.group.find({"group_name": group_name, "recommended_playlist": { "$exists": True }}):
            recommendedStatus = True
            recommended_playlist = result["recommended_playlist"]

    if recommendedStatus == False:
        return jsonify({"bool": recommendedStatus})
    
    return jsonify({"code": 200, "bool": recommendedStatus, "name": recommended_playlist["name"], "link": recommended_playlist["external_urls"]["spotify"], "cover": recommended_playlist["images"][0]["url"]})

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
        'Content-Type': 'application/json',
        'Authorization': f"Bearer {access_token}"
    }

    # Make the request to the Recommendations Microservice API endpoint
    response = requests.post(recommendations_URL, json=params, headers=headers).json()

    if response["code"] == 201:
        recommended_playlist_id = response["id"]

        playlist_info = requests.get(f'https://api.spotify.com/v1/playlists/{recommended_playlist_id}', headers=headers).json()

        result = db.group.update_one(
            {'group_name': group_name, "recommend_playlist": { "$exists": True }},
            {"$set": {"recommend_playlist": playlist_info}},
        )

        # if no documents are updated, add a new recommend_playlist field
        if result.modified_count == 0:
            update_new = {"$push": {"recommended_playlist": playlist_info}}
            result = db.group.update_one({"group_name": group_name}, update_new)

        print("recommended playlist added into mongoDB")
        return jsonify({"code": 201, "message": "recommended playlist successfully created"})
    
    print("error creating recommended playlist")
    return jsonify({"code": 500, "message": "recommended playlist creation not successful"})


@app.route("/api/v1/save_playlist", methods=['POST'])
def save_playlist():
    data = request.get_json()
    playlist_link = data.get('playlist_link')
    email = data.get('email')
    group_name = request.headers.get('group_name', '')
    playlist_id = re.search(r'playlist\/(\w+)', playlist_link).group(1)
    savedStatus = False

    # query for documents with a specific group name and user_and_playlist field not exists
    query = {"group_name": group_name, "user_and_playlist": {"$exists": False}}
    # add user_and_playlist field to the matched documents with an empty object as the value
    update = {"$set": {"user_and_playlist": []}}
    # update the documents matching the query
    result1 = db.group.update_one(query, update)

    # query for documents with a specific group name and user_and_playlist field containing the email key
    query = {"group_name": group_name, "user_and_playlist.email": email}
    # if a document is found, update the playlist_id value for the email key
    update_existing = {"$set": {"user_and_playlist.$.playlistID": playlist_id}}
    # update the documents matching the query
    result = db.group.update_one(query, update_existing)

    # if no documents are updated, add a new subdocument with the email and playlist_id
    if result.modified_count == 0:
        update_new = {"$push": {"user_and_playlist": {"email": email, "playlistID": playlist_id}}}
        result = db.group.update_one({"group_name": group_name}, update_new)

    savedStatus = True

    return jsonify(savedStatus)

if __name__ == "__main__":
    print("This is flask " + os.path.basename(__file__) + " for the group complex microservice...")
    app.run(host="0.0.0.0", port=4998, debug=True)
