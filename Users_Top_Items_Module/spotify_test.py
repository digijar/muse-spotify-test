# import spotipy
# import yaml
# from spotipy.oauth2 import SpotifyOAuth
import os
import random
from random import randint
import base64
import requests
from flask import Flask, request, jsonify, redirect, url_for, session, render_template, render_template_string
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

app = Flask(__name__, template_folder='templates')
app.secret_key = os.urandom(24)

@app.route('/')
def home():
    return render_template('index.html')

# @app.route('/login-api')
# def login_api():
#     params = {
#         'client_id': SPOTIFY_CLIENT_ID,
#         'response_type': 'code',
#         'redirect_uri': SPOTIFY_REDIRECT_URI,
#         'scope': 'user-read-private user-read-email user-top-read playlist-read-private playlist-read-collaborative playlist-modify-private playlist-modify-public',
#     }
#     auth_url = f'{SPOTIFY_AUTH_URL}?{urlencode(params)}'
#     return jsonify({"auth_url": auth_url})

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

        return jsonify({"top_artists": top_artists["items"], "top_tracks": top_tracks["items"]})
    else:
        return jsonify({"code": 400, "message": "Bad request. Missing access token."}), 400
    


@app.route('/recommendations')
def recommendations():

    access_token = request.headers.get('Authorization', '').replace('Bearer ', '')
    if not access_token and 'access_token' in session:
        access_token = session['access_token']

    if access_token:
        return render_template("recommendations.html", access_token=access_token)
    else:
        # Refresh the access token
        refresh_token = session.get('refresh_token')
        new_access_token = refresh_access_token(refresh_token)
        if new_access_token:
            access_token = new_access_token
            session['access_token'] = new_access_token
            return render_template("recommendations.html", access_token=new_access_token)
        
        else:
            return jsonify({"code": 400, "message": "Bad request. Missing access token."}), 400

@app.route('/generate_recommendations', methods=['POST'])
def generate_recommendations():
    access_token = request.headers.get('Authorization', '').replace('Bearer ', '')
    if not access_token and 'access_token' in session:
        access_token = session['access_token']

    if access_token:
        playlist_ids = request.json.get('playlist_ids', [])

        headers = {
            'Authorization': f"Bearer {access_token}"
        }

        user_data = requests.get('https://api.spotify.com/v1/me', headers=headers).json()
        user_id = user_data['id']

        # Create a new empty playlist
        playlist_randnum = randint(100,999)

        new_playlist_response = requests.post(
            f'https://api.spotify.com/v1/users/{user_id}/playlists',
            headers=headers,
            json={"name": f"Recommended Playlist {playlist_randnum}", 
                  "description": "trying not to break the Spotify API",
                  "public": "true"}
        )
        if new_playlist_response.status_code != 201:
            print("Error creating playlist:", new_playlist_response.status_code, new_playlist_response.text)
            return jsonify({"code": 500, "message": "An error occurred while creating the recommended playlist."}), 500

        new_playlist = new_playlist_response.json()

        # Extract tracks from input playlists
        all_tracks = []
        for playlist_id in playlist_ids:
            tracks = requests.get(f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks', headers=headers).json()
            all_tracks.extend(tracks['items'])

        # Extract artist IDs from the input playlist tracks
        artist_ids = list(set([track['track']['artists'][0]['id'] for track in all_tracks]))

        # Fetch genres associated with the artists
        seed_genres = []
        for i in range(0, len(artist_ids), 50):
            response = requests.get(
                f'https://api.spotify.com/v1/artists?ids={",".join(artist_ids[i:i+50])}',
                headers=headers
            )
            try:
                artists_data = response.json()
            except requests.exceptions.JSONDecodeError:
                print(f"Error decoding JSON response: {response.text}")
                continue

            if 'artists' in artists_data:
                for artist in artists_data['artists']:
                    seed_genres.extend(artist['genres'])
            else:
                print(f"Unexpected response format: {artists_data}")
                # Remove duplicate genres
                seed_genres = list(set(seed_genres))

        # Generate recommendations based on input playlist tracks
        recommended_tracks = requests.get(
            'https://api.spotify.com/v1/recommendations',
            params={
                'seed_genres': ','.join(random.sample(seed_genres, min(len(seed_genres), 5))),
                'seed_tracks': ','.join(random.sample([track['track']['id'] for track in all_tracks], min(len(all_tracks), 5))),
                # 'seed_artists': ','.join(random.sample(artist_ids, min(len(artist_ids), 5))),
                'limit': 50,
            },
            headers=headers
        ).json()

        if 'tracks' not in recommended_tracks:
            print(f"Unexpected response format: {recommendations}")

            return jsonify({"code": 500, "message": "An error occurred while fetching recommendations."}), 500

        # Add recommended tracks to the new playlist
        track_uris = [track['uri'] for track in recommended_tracks['tracks']]
        requests.post(
            f'https://api.spotify.com/v1/playlists/{new_playlist["id"]}/tracks',
            headers=headers,
            json={"uris": track_uris}
        )

        return jsonify({"name": new_playlist["name"]})
    else:
        return jsonify({"code": 400, "message": "Bad request. Missing access token."}), 400



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

if __name__ == '__main__':
    print("This is flask for " + os.path.basename(__file__) + ": manage Spotify Authorization Code Flow ...")
    app.run(host='0.0.0.0', port=5001, debug=True)