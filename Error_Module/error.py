# all imports
import os
from random import randint
import requests
from flask import Flask, request, jsonify, redirect, url_for, session
from urllib.parse import urlencode
import json
from flask import session
from flask_cors import CORS
import pymongo
from pymongo import MongoClient
import amqp_setup
import pika
import json

# for API Keys
from dotenv import load_dotenv
load_dotenv('spotify_api_keys.env')

username = os.getenv('username')
password = os.getenv('password')

### Connecting to MongoDB
mongo_uri = f"mongodb+srv://{username}:{password}@musecluster.egcmgf4.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(mongo_uri, ssl=True, tlsAllowInvalidCertificates=True)
db = client.ESD_Muse

app = Flask(__name__)
CORS(app)
app.secret_key = os.urandom(24)

@app.route("/api/v1/error", methods=['POST'])
def receiveError():
    amqp_setup.check_setup()
    queue_name = "Error"  
    amqp_setup.channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
    while True:
        try:
            amqp_setup.connection.process_data_events(time_limit=1)
        except pika.exceptions.ConnectionClosed:
            return
        except KeyboardInterrupt:
            amqp_setup.channel.stop_consuming()
            break

    # Return success response
    return jsonify({"message": "Error sent to error microservice"}), 200

def callback(channel, method, properties, body):
    print("\nReceived an error by " + __file__)
    processError(body)
    print()

def processError(errorMsg):
    print("Printing the error message:")
    try:
        error = json.loads(errorMsg)
        print("--JSON:", error)

        # adding into mongoDB error_log collection for future reference
        db.error_log.insert_one(
            {   
                "email": "digijar@live.com",
                "code": error["code"],
                "message": error["message"]
            }
        )

    except Exception as e:
        print("--NOT JSON:", e)
        print("--DATA:", errorMsg)
    print()

### setting flask host and port
if __name__ == '__main__':
    print("This is flask for " + os.path.basename(__file__) + ": muse's errors ...")
    app.run(host='0.0.0.0', port=4997, debug=True)