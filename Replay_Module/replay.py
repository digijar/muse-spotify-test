# all imports
import os
from random import randint
import requests
from flask import Flask, request, jsonify, redirect, url_for, session
from urllib.parse import urlencode
import json
from flask import session
from flask_cors import CORS
import pymongo
from pymongo import MongoClient

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

app = Flask(__name__)
CORS(app)
app.secret_key = os.urandom(24)

@app.route('/replay/get_top_tracks')
def replay_get_top_tracks():
    data = request.args
    email = data.get('Email')
    result = db.top_artists.find_one(
        {'user': email},
        {'top_tracks': 1, '_id': 0}
    )

    return jsonify(result['top_tracks'])

@app.route('/replay/get_top_artists')
def replay_get_top_artists():
    data = request.args
    email = data.get('Email')
    result = db.top_artists.find_one(
        {'user': email},
        {'top_artists': 1, '_id': 0}
    )

    return jsonify(result['top_artists'])


@app.route('/replay/reload_top_items')
def replay_reload_top_items():
    data = request.args
    email = data.get('Email')
    access_token = data.get('access_token')

    result = db.top_artists.find_one(
        {'user': email},
    )

    if result == None:
        return insert_top_artists_tracks_data(access_token)
    
    return update_top_artists_tracks_data(access_token)

def update_top_artists_tracks_data(access_token):
    if not access_token and 'access_token' in session:
        access_token = session['access_token']

    if access_token:
        headers = {
            'Authorization': f"Bearer {access_token}"
        }
        top_artists = requests.get('https://api.spotify.com/v1/me/top/artists', headers=headers).json()
        top_tracks = requests.get('https://api.spotify.com/v1/me/top/tracks', headers=headers).json()
        user_profile = requests.get('https://api.spotify.com/v1/me', headers=headers).json()
        user_email = user_profile["email"]

        # Get a handle to the Top_Artists collection
        Top_Artists = db.top_artists

        # updating instance in collection
        result = Top_Artists.update_one(
            {'user': user_email},
            {"$set": {"top_artists": top_artists, "top_tracks": top_tracks}, "$currentDate": {"lastModified": True}},
        )

        if result.modified_count == 1:
            return jsonify({"code": 200, "message": "User's Top artists and tracks updated successfully."}), 200
    else:
        return jsonify({"code": 400, "message": "Bad request. Missing access token."}), 400

def insert_top_artists_tracks_data(access_token):
    if not access_token and 'access_token' in session:
        access_token = session['access_token']

    if access_token:
        headers = {
            'Authorization': f"Bearer {access_token}"
        }
        top_artists = requests.get('https://api.spotify.com/v1/me/top/artists', headers=headers).json()
        top_tracks = requests.get('https://api.spotify.com/v1/me/top/tracks', headers=headers).json()
        user_profile = requests.get('https://api.spotify.com/v1/me', headers=headers).json()
        user_email = user_profile["email"]

        # Get a handle to the Top_Artists collection
        Top_Artists = db.top_artists

        # inserting instance into collection
        users_top_artist = {'user': user_email, 
                            'top_artists': top_artists,
                            'top_tracks': top_tracks}
        Top_Artists.insert_one(users_top_artist)

        return jsonify({"code": 200, "top_artists": top_artists["items"], "top_tracks": top_tracks["items"]})
    else:
        return jsonify({"code": 400, "message": "Bad request. Missing access token."}), 400

### setting flask host and port
if __name__ == '__main__':
    print("This is flask for " + os.path.basename(__file__) + ": manage Spotify Authorization Code Flow ...")
    app.run(host='0.0.0.0', port=5001, debug=True)