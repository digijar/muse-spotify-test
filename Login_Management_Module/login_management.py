# all imports
from flask import Flask, request, jsonify, session
from flask_cors import CORS
import os
from os import environ
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

### Connecting to MongoDB
mongo_uri = f"mongodb+srv://{user}:{password}@musecluster.egcmgf4.mongodb.net/?retryWrites=true&w=majority"

# Create a MongoDB client and connect to the sample_training database
client = MongoClient(mongo_uri, ssl=True, tlsAllowInvalidCertificates=True)
db = client.ESD_Muse


@app.route("/api/v1/mongo_authenticate", methods = ['POST'])
def mongo_authenticate():
    email = request.json.get('email', '')
    password = request.json.get('password', '')
    payload = {'email': email, 'password': password}
    headers = {'Content-Type': 'application/json'}
    access_token_info = requests.post('http://auth:5003/auth/authenticate', json=payload, headers=headers).json()
    print(access_token_info)
    return jsonify(access_token_info)

@app.route("/api/v1/mongo_createUser", methods = ['POST'])
def mongo_createUser():
    email = request.json.get('email', '')
    password = request.json.get('password', '')
    payload = {'email': email, 'password': password}
    headers = {'Content-Type': 'application/json'}
    sign_up_info = requests.post('http://auth:5003/auth/createUser', json=payload, headers=headers).json()
    print(sign_up_info)
    return jsonify(sign_up_info)

@app.route("/api/v1/login")
def login():
    code = request.args.get('code')
    data = {
        'code': code
    }
    access_token_info = requests.get('http://authentication:5002/authenticate/login', params=data).json()
    print(access_token_info)
    return jsonify(access_token_info)

@app.route("/api/v1/refresh", methods=['POST'])
def refresh():
    refresh_token = request.json['refresh_token']
    data = {
        'refresh_token': refresh_token
    }
    refresh_token_info = requests.post('http://authentication:5002/authenticate/refresh', data=data).json()
    print(refresh_token_info)
    return jsonify(refresh_token_info)

@app.route("/api/v1/email")
def email():
    access_token = request.headers.get('Authorization', '').replace('Bearer ', '')
    data = {
        'access_token': access_token
    }
    email_info = requests.get('http://authentication:5002/authenticate/email', params=data).json()
    print(email_info)
    return jsonify(email_info)


if __name__ == "__main__":
    print("This is flask " + os.path.basename(__file__) + " for the 'Login Management' complex microservice...")
    app.run(host="0.0.0.0", port=5006, debug=True)