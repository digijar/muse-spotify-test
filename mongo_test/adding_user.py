import os
import pymongo
from pymongo import MongoClient

# for flask
import random
from random import randint
import base64
import requests
from flask import Flask, request, jsonify, redirect, url_for, session, render_template, render_template_string
from urllib.parse import urlencode
import json
from flask import session

# load username & password
from dotenv import load_dotenv
load_dotenv('mongo_test.env')

username = os.getenv('username')
password = os.getenv('password')

# Replace the placeholder string with your MongoDB connection string
mongo_uri = f"mongodb+srv://{username}:${password}@musecluster.egcmgf4.mongodb.net/?retryWrites=true&w=majority"

# Create a MongoDB client and connect to the sample_training database
client = MongoClient(mongo_uri, ssl=True, tlsAllowInvalidCertificates=True)
db = client.ESD_Muse

# Get a handle to the User collection
User_collection = db.User



# Insert a user
# user = {'name': 'John Doe', 'email': 'johndoe@example.com','GroupId':'1','PlaylistId':'blablabla'}
# result = User_collection.insert_one(user)