# all imports
from flask import Flask, request, jsonify, session
from flask_cors import CORS
import os
import requests
import pymongo
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)
app.secret_key = os.urandom(24)

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

# for PlaylistCard component on BlendPage component which is on GroupBlendView
@app.route("/group/get_groups")
def group_get_groups():
    data = request.args
    email = data.get('Email')
    group_names = []
    for result in db.group.find({}):
        if email in result["friends"]:
            group_names.append(result["group_name"])

    return jsonify(group_names)

# for InviteFriend component on BlendView
@app.route("/group/get_friends")
def group_get_friends():
    data = request.args
    email = data.get('Email')
    print(email)
    group_name = data.get('group_name')

    friend_names = []
    for result in db.group.find({"group_name": group_name}):
        for name in result["friends"]:
            if name != email:
                friend_names.append(name)

    return jsonify(friend_names)


# checks whether user has uploaded
@app.route("/group/check_personalUpload")
def group_check_personalUpload():
    data = request.args
    access_token = data.get('access_token')
    group_name = data.get('group_name')
    email = data.get('email')

    personalUpload = False
    playlistID = ""
    for result in db.group.find({"group_name": group_name, "user_and_playlist": { "$exists": True }}):
        print("group found!")
        if len(result["user_and_playlist"]) > 0:
            for emails in result["user_and_playlist"]:
                if email == emails["email"]:
                    personalUpload = True
                    playlistID = emails["playlistID"]

    ## get uploaded playlist details
    if personalUpload == True and playlistID != "":
        print('successfully retrieved user information from Mongo!')
        print(playlistID)
        headers = {
            "Content-Type": "application/json",
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

@app.route("/group/check_groupStatus")
def group_check_groupStatus():
    data = request.args
    group_name = data.get('group_name')

    groupStatus = False
    user_and_playlist_arr = []

    for result in db.group.find({"group_name": group_name, "user_and_playlist": { "$exists": True }}):
        if len(result["user_and_playlist"]) == len(result["friends"]):
            groupStatus = True
            for arr in result["user_and_playlist"]:
                user_and_playlist_arr.append(arr["playlistID"])

    return jsonify({"bool": groupStatus, "playlist_arr": user_and_playlist_arr})

@app.route("/group/check_recommendedStatus")
def group_check_recommendedStatus():
    data = request.args
    group_name = data.get('group_name')

    recommendedStatus = False
    recommended_playlist = {}
    for result in db.group.find({"group_name": group_name, "recommended_playlist": { "$exists": True }}):
        if len(result['recommended_playlist']) > 0:
            recommendedStatus = True
            recommended_playlist = result["recommended_playlist"]

    if recommendedStatus == False:
        return jsonify({"bool": recommendedStatus})
    
    return jsonify({"code": 200, "bool": recommendedStatus, "name": recommended_playlist["name"], "link": recommended_playlist["external_urls"]["spotify"], "cover": recommended_playlist["images"][0]["url"]})


@app.route("/group/save_playlist", methods=['POST'])
def group_save_playlist():
    data = request.form
    email = data.get('Email')
    group_name = data.get('group_name')
    playlist_id = data.get('playlist_id')
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
        print("pushing new email and playlistID key:value pair into user_and_playlist array!")
        update_new = {"$push": {"user_and_playlist": {"email": email, "playlistID": playlist_id}}}
        result = db.group.update_one({"group_name": group_name}, update_new)
        savedStatus = True
    if result.modified_count != 0:
        savedStatus = True

    return jsonify(savedStatus)


####### Creating Group #########
@app.route("/group/create_group", methods=['POST'])
def group_create_group():
    data = request.form
    email = data.get('Email')
    group_name = data.get('group_name')

    result = db.group.insert_one(
        {
            "friends": [email],
            "group_name": group_name,
            "user_and_playlist": [],
        }
    )

    if result.inserted_id:
        print("group successfully created")
        return jsonify({"code": 201, "message": "group successfully created!"}), 201
    
    print("group creation not successful :<")
    return jsonify({"code": 400, "message": "group creation not successful :<"})



#### technical function remove recommended playlist #####
@app.route("/group/remove_playlist", methods=['POST'])
def group_remove_playlist():
    data = request.form
    group_name = data.get('group_name')
    removedStatus = False
    result = db.group.update_one(
        {'group_name': group_name, "recommended_playlist": { "$exists": True }},
        {"$set": {"recommended_playlist": {}}},
    )
    if result.modified_count != 0:
        removedStatus = True
    return jsonify(removedStatus)

@app.route("/group/remove_friend", methods=['POST'])
def group_remove_friend():
    data = request.form
    group_name = data.get('group_name')
    friend_email = data.get('friend_email')
    removedStatus = False

    result = db.group.update_one(
        {"group_name": group_name},
        {"$pull": {"friends": friend_email}}
    )
    if result.modified_count != 0:
        removedStatus = True
    return jsonify(removedStatus)




if __name__ == "__main__":
    print("This is flask " + os.path.basename(__file__) + " for the group simple microservice...")
    app.run(host="0.0.0.0", port=4998, debug=True)
