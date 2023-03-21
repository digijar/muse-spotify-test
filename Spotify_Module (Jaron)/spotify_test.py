# import spotipy
# import yaml
# from spotipy.oauth2 import SpotifyOAuth
import os
import base64
import requests
from flask import Flask, request, jsonify, redirect
from urllib.parse import urlencode
import json
from flask import session


# from spotify_functions import offset_api_limit, get_artists_df, get_tracks_df, get_track_audio_df,\
#     get_all_playlist_tracks_df, get_recommendations


# with open("spotify_details.yml", 'r') as stream:
#     spotify_details = yaml.safe_load(stream)

# # https://developer.spotify.com/web-api/using-scopes/
# scope = "user-library-read user-follow-read user-top-read playlist-read-private"

# sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
#     client_id=spotify_details['client_id'],
#     client_secret=spotify_details['client_secret'],
#     redirect_uri=spotify_details['redirect_uri'],
#     scope=scope,
# ))

# Set your Spotify API credentials here
# retrieving API Key from .env file
from dotenv import load_dotenv
load_dotenv('spotify_api_keys.env')

SPOTIFY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
SPOTIFY_CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')
SPOTIFY_REDIRECT_URI = os.getenv('SPOTIFY_REDIRECT_URI')
SPOTIFY_AUTH_URL = 'https://accounts.spotify.com/authorize'
SPOTIFY_TOKEN_URL = 'https://accounts.spotify.com/api/token'

app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY')

@app.route('/login')
def login():
    params = {
        'client_id': SPOTIFY_CLIENT_ID,
        'response_type': 'code',
        'redirect_uri': SPOTIFY_REDIRECT_URI,
        'scope': 'user-read-private user-read-email user-top-read',
    }
    auth_url = f'{SPOTIFY_AUTH_URL}?{urlencode(params)}'
    return redirect(auth_url)

@app.route('/callback')
def callback():
    code = request.args.get('code')
    if code:
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
            session['refresh_token'] = tokens['refresh_token']
            return redirect('/top_artists_tracks')
        else:
            return jsonify({"code": response.status_code, "message": "An error occurred while exchanging the authorization code for an access token."}), response.status_code

    else:
        return jsonify({"code": 400, "message": "Bad request. Missing authorization code."}), 400

@app.route('/top_artists_tracks')
def top_artists_tracks():
    headers = {
        'Authorization': f"Bearer {session['access_token']}"
    }
    top_artists = requests.get('https://api.spotify.com/v1/me/top/artists', headers=headers).json()
    top_tracks = requests.get('https://api.spotify.com/v1/me/top/tracks', headers=headers).json()

    return jsonify({"top_artists": top_artists, "top_tracks": top_tracks})

if __name__ == '__main__':
    print("This is flask for " + os.path.basename(__file__) + ": manage Spotify Authorization Code Flow ...")
    app.run(host='0.0.0.0', port=5001, debug=True)