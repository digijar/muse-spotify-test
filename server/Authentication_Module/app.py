from flask import Flask, request, redirect, session, jsonify, Blueprint
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv

# Load Spotify app credentials from .env file
load_dotenv('spotify_api_keys.env')

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Spotify app credentials
SPOTIPY_CLIENT_ID = os.environ.get('SPOTIFY_CLIENT_ID')
SPOTIPY_CLIENT_SECRET = os.environ.get('SPOTIFY_CLIENT_SECRET')
SPOTIPY_REDIRECT_URI = os.environ.get('SPOTIFY_REDIRECT_URI')
SCOPE = 'user-read-private user-read-email'

# Create a SpotifyOAuth instance
sp_oauth = SpotifyOAuth(
    client_id=SPOTIPY_CLIENT_ID,
    client_secret=SPOTIPY_CLIENT_SECRET,
    redirect_uri=SPOTIPY_REDIRECT_URI,
    scope=SCOPE
)

# Blueprint for authentication routes
auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/api/login')
def login():
    auth_url = sp_oauth.get_authorize_url()
    return redirect(auth_url)

@auth_bp.route('/api/callback')
def callback():
    code = request.args.get('code')
    token_info = sp_oauth.get_access_token(code)
    session['access_token'] = token_info['access_token']
    session['refresh_token'] = token_info['refresh_token']
    return redirect('/')

@auth_bp.route('/api/logout')
def logout():
    session.clear()
    return jsonify({'message': 'Logged out successfully'})

@auth_bp.route('/api/user')
def user():
    if 'access_token' not in session:
        return redirect('/login')
    sp = spotipy.Spotify(auth=session['access_token'])
    user = sp.current_user()
    return jsonify(user)

# Register the auth blueprint
app.register_blueprint(auth_bp, url_prefix='/auth')

if __name__ == '__main__':
    app.run(debug=True, port="2504")