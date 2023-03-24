# all imports
import os
import random
from random import randint
import base64
import requests
from flask import Flask, request, jsonify, redirect, url_for, session, render_template, render_template_string
from urllib.parse import urlencode
import json
from flask import session

# for API Keys
from dotenv import load_dotenv
load_dotenv('spotify_api_keys.env')

SPOTIFY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
SPOTIFY_CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')
SPOTIFY_REDIRECT_URI = os.getenv('SPOTIFY_REDIRECT_URI')
SPOTIFY_AUTH_URL = 'https://accounts.spotify.com/authorize'
SPOTIFY_TOKEN_URL = 'https://accounts.spotify.com/api/token'

app = Flask(__name__, template_folder='templates')
app.secret_key = os.urandom(24)

@app.route('/api/v1/login')
def login():
    params = {
        'client_id': SPOTIFY_CLIENT_ID,
        'response_type': 'code',
        'redirect_uri': SPOTIFY_REDIRECT_URI,
        'scope': 'user-read-private user-read-email user-top-read playlist-read-private playlist-read-collaborative playlist-modify-private playlist-modify-public',
    }
    auth_url = f'{SPOTIFY_AUTH_URL}?{urlencode(params)}'
    return redirect(auth_url)

@app.route('/api/v1/callback')
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
            return redirect('http://localhost:5173', messages={"main":"Condition failed on page baz"})
        else:
            return jsonify({"code": response.status_code, "message": "An error occurred while exchanging the authorization code for an access token."}), response.status_code


### For Logging OUT
@app.route('/api/v1/logout')
def logout():
    session.clear()
    return jsonify({'message': 'Logged out successfully'})

### For getting user
# @app.route('/api/v1/user')
# def user():
#     if 'access_token' not in session:
#         return redirect('/login')
#     sp = spotipy.Spotify(auth=session['access_token'])
#     user = sp.current_user()
#     return jsonify(user)

### For Refresh Tokens
def refresh_access_token(refresh_token):
    data = {
        'grant_type': 'refresh_token',
        'refresh_token': refresh_token,
        'client_id': SPOTIFY_CLIENT_ID,
        'client_secret': SPOTIFY_CLIENT_SECRET
    }

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    token_response = requests.post(SPOTIFY_TOKEN_URL, data=data, headers=headers)
    token_info = token_response.json()

    if 'access_token' in token_info:
        return token_info['access_token']
    else:
        return None


### setting flask host and port
if __name__ == '__main__':
    print("This is flask for " + os.path.basename(__file__) + ": manage Spotify Authorization Code Flow ...")
    app.run(host='0.0.0.0', port=2504, debug=True)