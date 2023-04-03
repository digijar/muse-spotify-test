# all imports
import os
import random
from random import randint
import requests
import json
from datetime import datetime, timedelta
from flask import Flask, request, jsonify, session
from flask_cors import CORS
import base64

# for API Keys
from dotenv import load_dotenv
load_dotenv('spotify_api_keys.env')

SPOTIFY_AUTH_ENDPOINT = 'https://accounts.spotify.com/api/token'
CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')
REDIRECT_URI = os.getenv('SPOTIFY_REDIRECT_URI')

app = Flask(__name__)
CORS(app, resources={r"*": {"origins": "*"}})
app.secret_key = os.urandom(24)

def get_auth_token(code):
    client_creds = f'{CLIENT_ID}:{CLIENT_SECRET}'
    client_creds_64 = base64.b64encode(client_creds.encode())
    headers = {
        'Authorization': f'Basic {client_creds_64.decode()}',
        'Content-Type': 'application/x-www-form-urlencoded'}
    data = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': REDIRECT_URI,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET
    }

    response = requests.post(SPOTIFY_AUTH_ENDPOINT, headers=headers, data=data)
    response_data = response.json()

    return response_data['access_token'], response_data['refresh_token'], response_data['expires_in']

def refresh_auth_token(refresh_token):
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    data = {
        'grant_type': 'refresh_token',
        'refresh_token': refresh_token,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET
    }

    response = requests.post(SPOTIFY_AUTH_ENDPOINT, headers=headers, data=data)
    response_data = json.loads(response.text)

    return response_data['access_token'], response_data['expires_in']

@app.route('/authenticate/login')
def authenticate_login():
    code = request.args.get('code')

    if not code:
        return jsonify({'error': 'Missing authorization code'})

    auth_token, refresh_token, expires_in = get_auth_token(code)

    # Calculate the expiry time of the authorization token
    expiry_time = datetime.now() + timedelta(seconds=expires_in)

    response_data = {
        'auth_token': auth_token,
        'refresh_token': refresh_token,
        'expiry_time': expiry_time.timestamp()
    }

    response = jsonify(response_data)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/authenticate/refresh', methods=['POST'])
def authenticate_refresh():
    data = request.form
    refresh_token = data.get('refresh_token')

    if not refresh_token:
        return jsonify({'error': 'Missing refresh token'})

    auth_token, expires_in = refresh_auth_token(refresh_token)

    # Calculate the expiry time of the new authorization token
    expiry_time = datetime.now() + timedelta(seconds=expires_in)

    response_data = {
        'auth_token': auth_token,
        'expiry_time': expiry_time.timestamp()
    }

    response = jsonify(response_data)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/authenticate/email')
def authenticate_email():
    access_token = request.args.get('access_token')
    if not access_token and 'access_token' in session:
        access_token = session['access_token']

    if access_token:
        payload={}
        headers = {
            'Authorization': f"Bearer {access_token}",
            'Content-Type': 'application/json'
        }
        # user_profile = requests.get('https://api.spotify.com/v1/me', headers=headers).json()
        user_profile = requests.request("GET", 'https://api.spotify.com/v1/me', headers=headers, data=payload).json()
        user_email = user_profile["email"]

        response_data = {
            'email': user_email
        }
        
        return response_data
    
    else:
        return jsonify({"code": 400, "message": "Bad request. Missing access token."}), 400


### setting flask host and port
if __name__ == '__main__':
    print("This is flask for " + os.path.basename(__file__) + ": manage Spotify Authorization Code Flow ...")
    app.run(host='0.0.0.0', port=5002, debug=True)