# all imports
import os
import random
from random import randint
import base64
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

app = Flask(__name__)
CORS(app)
app.secret_key = os.urandom(24)

@app.route('/api/v1/get_top_tracks')
def get_top_tracks():

    result = db.top_artists.find_one(
        {'user': 'digijar@live.com'},
        {'top_tracks': 1, '_id': 0}
    )

    return jsonify(result['top_tracks'])

@app.route('/api/v1/get_top_artists')
def get_top_artists():

    result = db.top_artists.find_one(
        {'user': 'digijar@live.com'},
        {'top_artists': 1, '_id': 0}
    )

    return jsonify(result['top_artists'])

# @app.route('/login')
# def login():
#     params = {
#         'client_id': SPOTIFY_CLIENT_ID,
#         'response_type': 'code',
#         'redirect_uri': SPOTIFY_REDIRECT_URI,
#         'scope': 'user-read-private user-read-email user-top-read playlist-read-private playlist-read-collaborative playlist-modify-private playlist-modify-public',
#     }
#     auth_url = f'{SPOTIFY_AUTH_URL}?{urlencode(params)}'
#     return redirect(auth_url)

# @app.route('/callback')
# def callback():
#     code = request.args.get('code')
#     if code:
#         # Code for exchanging the authorization code for an access token
#         token_data = {
#             'grant_type': 'authorization_code',
#             'code': code,
#             'redirect_uri': SPOTIFY_REDIRECT_URI,
#             'client_id': SPOTIFY_CLIENT_ID,
#             'client_secret': SPOTIFY_CLIENT_SECRET
#         }
#         response = requests.post(SPOTIFY_TOKEN_URL, data=token_data)

#         if response.status_code == 200:
#             tokens = response.json()
#             session['access_token'] = tokens['access_token']
#             session['refresh_token'] = tokens['refresh_token']  # Store the refresh token
#             return redirect('/top_artists_tracks')
#         else:
#             return jsonify({"code": response.status_code, "message": "An error occurred while exchanging the authorization code for an access token."}), response.status_code

# @app.route('/top_artists_tracks')
# def top_artists_tracks():
#     access_token = request.headers.get('Authorization', '').replace('Bearer ', '')
#     if not access_token and 'access_token' in session:
#         access_token = session['access_token']

#     if access_token:
#         # return render_template("top_artists_tracks.html", access_token=access_token)
#     else:
#         return jsonify({"code": 400, "message": "Bad request. Missing access token."}), 400

# @app.route('/api/v1/top_artists')
# def top_artists():
#     access_token = request.headers.get('Authorization', '').replace('Bearer ', '')
#     if not access_token and 'access_token' in session:
#         access_token = session['access_token']

#     if access_token:
#         headers = {
#             'Authorization': f"Bearer {access_token}"
#         }
#         top_artists = requests.get('https://api.spotify.com/v1/me/top/artists', headers=headers).json()

#         return jsonify({"top_artists": top_artists})
#     else:
#         return jsonify({"code": 400, "message": "Bad request. Missing access token."}), 400

# @app.route('/api/v1/top_artists_tracks_data')
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


### For Refresh Tokens
# def refresh_access_token(refresh_token):
#     data = {
#         'grant_type': 'refresh_token',
#         'refresh_token': refresh_token,
#         'client_id': SPOTIFY_CLIENT_ID,
#         'client_secret': SPOTIFY_CLIENT_SECRET
#     }

#     headers = {
#         'Content-Type': 'application/x-www-form-urlencoded'
#     }

#     token_response = requests.post(SPOTIFY_TOKEN_URL, data=data, headers=headers)
#     token_info = token_response.json()

#     if 'access_token' in token_info:
#         return token_info['access_token']
#     else:
#         return None

### setting flask host and port
if __name__ == '__main__':
    print("This is flask for " + os.path.basename(__file__) + ": manage Spotify Authorization Code Flow ...")
    app.run(host='0.0.0.0', port=5001, debug=True)