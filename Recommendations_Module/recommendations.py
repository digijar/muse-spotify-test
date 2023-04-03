# all imports
import os
import random
from random import randint
import requests
from flask import Flask, request, jsonify
from flask_cors import CORS

# for API Keys
from dotenv import load_dotenv
load_dotenv('spotify_api_keys.env')

SPOTIFY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
SPOTIFY_CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')
SPOTIFY_REDIRECT_URI = os.getenv('SPOTIFY_REDIRECT_URI')
SPOTIFY_AUTH_URL = 'https://accounts.spotify.com/authorize'
SPOTIFY_TOKEN_URL = 'https://accounts.spotify.com/api/token'

app = Flask(__name__, template_folder='templates')
CORS(app)
app.secret_key = os.urandom(24)

################### MAIN FUNCTION ###################
@app.route('/generate_recommendations', methods=['POST'])
def generate_recommendations():
    # access_token = request.headers.get('Authorization', '').replace('Bearer ', '')
    access_token = request.headers.get('access_token')
    playlist_ids = request.headers.get('playlist_ids')
    print(access_token)
    print(playlist_ids)
    playlist_ids = playlist_ids.split(',')

    if access_token:
        headers = {
            "Content-Type": "application/json",
            "Authorization": request.headers.get('Authorization')
        }

        print("getting user's data")
        print()
        user_data = requests.get('https://api.spotify.com/v1/me', headers=headers).json()
        user_id = user_data['id']

        # Create a new empty playlist
        playlist_randnum = randint(100,999)

        print("creating new playlist")
        print()
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
        
        print("getting tracks from all playlists inputted")
        print()
        for playlist_id in playlist_ids:
            tracks_response = requests.get(f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks', headers=headers)
            if tracks_response.status_code != 200:
                print("Error getting tracks:", tracks_response.status_code, tracks_response.text)
                return jsonify({"code": 500, "message": "An error occurred while getting tracks."}), 500
            else:
                tracks = tracks_response.json()
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
        print("getting recommendations")
        print()
        recommended_tracks = requests.get(
            'https://api.spotify.com/v1/recommendations',
            params={
                'seed_genres': ','.join(random.sample(seed_genres, min(len(seed_genres), 3))),
                'seed_tracks': ','.join(random.sample([track['track']['id'] for track in all_tracks], min(len(all_tracks), 1))),
                'seed_artists': ','.join(random.sample(artist_ids, min(len(artist_ids), 1))),
                'limit': 50
            },
            headers=headers
        ).json()

        if 'tracks' not in recommended_tracks:
            print(f"Unexpected response format")

            return jsonify({"code": 500, "message": "An error occurred while fetching recommendations."}), 500

        # Add recommended tracks to the new playlist
        print("adding tracks to created playlist")
        print()
        track_uris = [track['uri'] for track in recommended_tracks['tracks']]
        requests.post(
            f'https://api.spotify.com/v1/playlists/{new_playlist["id"]}/tracks',
            headers=headers,
            json={"uris": track_uris}
        )

        return jsonify({"code": 201, "name": new_playlist["name"], "link": new_playlist["external_urls"]["spotify"], "id": new_playlist["id"]}), 201
    else:
        return jsonify({"code": 400, "message": "Bad request. Missing access token."}), 400


### setting flask host and port
if __name__ == '__main__':
    print("This is flask for " + os.path.basename(__file__) + ": manage Spotify Authorization Code Flow ...")
    app.run(host='0.0.0.0', port=5000, debug=True)