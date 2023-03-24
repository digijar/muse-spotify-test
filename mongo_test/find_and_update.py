# all imports
import os
import random
from random import randint
import base64
import requests
from flask import Flask, request, jsonify, redirect, url_for, session, render_template
from urllib.parse import urlencode
import json
from flask import session
import pymongo
from pymongo import MongoClient

# load username & password
from dotenv import load_dotenv
load_dotenv('mongo_test.env')

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


### Setting up Flask
app = Flask(__name__, template_folder='templates')
app.secret_key = os.urandom(24)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    params = {
        'client_id': SPOTIFY_CLIENT_ID,
        'response_type': 'code',
        'redirect_uri': SPOTIFY_REDIRECT_URI,
        'scope': 'user-read-private user-read-email user-top-read playlist-read-private playlist-read-collaborative playlist-modify-private playlist-modify-public',
    }
    auth_url = f'{SPOTIFY_AUTH_URL}?{urlencode(params)}'
    return redirect(auth_url)

@app.route('/callback')
def callback():
    code = request.args.get('code')
    if code:
        # Code for exchanging the authorization code for an access token
        token_data = {
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': SPOTIFY_REDIRECT_URI,
            'client_id': SPOTIFY_CLIENT_ID,
            'client_secret': SPOTIFY_CLIENT_SECRET
        }
        response = requests.post(SPOTIFY_TOKEN_URL, data=token_data)

        if response.status_code == 200:
            tokens = response.json()
            session['access_token'] = tokens['access_token']
            session['refresh_token'] = tokens['refresh_token']  # Store the refresh token
            return redirect('/top_artists_tracks')
        else:
            return jsonify({"code": response.status_code, "message": "An error occurred while exchanging the authorization code for an access token."}), response.status_code

@app.route('/top_artists_tracks')
def top_artists_tracks():
    access_token = request.headers.get('Authorization', '').replace('Bearer ', '')
    if not access_token and 'access_token' in session:
        access_token = session['access_token']

    if access_token:
        return render_template("top_artists_tracks.html", access_token=access_token)
    else:
        return jsonify({"code": 400, "message": "Bad request. Missing access token."}), 400


@app.route('/top_artists_tracks_data')
def top_artists_tracks_data():
    access_token = request.headers.get('Authorization', '').replace('Bearer ', '')
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

        # finding and updating instance into collection
        Top_Artists.replace_one

        return jsonify({"top_artists": top_artists["items"], "top_tracks": top_tracks["items"]})
    else:
        return jsonify({"code": 400, "message": "Bad request. Missing access token."}), 400



# @app.route('/top_artists_tracks_data')
# def top_artists_tracks_data():
#     access_token = request.headers.get('Authorization', '').replace('Bearer ', '')
#     if not access_token and 'access_token' in session:
#         access_token = session['access_token']

#     if access_token:
#         headers = {
#             'Authorization': f"Bearer {access_token}"
#         }
#         top_artists = requests.get('https://api.spotify.com/v1/me/top/artists', headers=headers).json()
#         top_tracks = requests.get('https://api.spotify.com/v1/me/top/tracks', headers=headers).json()

#         return jsonify({"top_artists": top_artists["items"], "top_tracks": top_tracks["items"]})
#     else:
#         return jsonify({"code": 400, "message": "Bad request. Missing access token."}), 400

### setting flask host and port


if __name__ == '__main__':
    print("This is flask for " + os.path.basename(__file__) + ": manage Spotify Authorization Code Flow ...")
    app.run(host='0.0.0.0', port=5002, debug=True)