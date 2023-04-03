# all imports
import os
import json
from flask import Flask, request, jsonify
import sendgrid
from sendgrid.helpers.mail import *
import twilio
from twilio.rest import Client
from flask_cors import CORS
import amqp_setup
import pika

# retrieving API Key from .env file
from dotenv import load_dotenv
load_dotenv('twillo_api_keys.env')

API_KEY = os.getenv('SENDGRID_API_KEY')
account_sid = os.getenv('TWILLO_ACCOUNT_SID')
auth_token = os.getenv('TWILLO_AUTH_TOKEN')

app = Flask(__name__)
CORS(app)

result = None

@app.route("/api/v1/email", methods=['POST'])
def receiveNotifications():
    global result
    result = None

    amqp_setup.check_setup()
    queue_name = 'Notifications'
    amqp_setup.channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
    while result is None:
        try:
            amqp_setup.connection.process_data_events(time_limit=1)
        except pika.exceptions.ConnectionClosed:
            return
        except KeyboardInterrupt:
            amqp_setup.channel.stop_consuming()
            break

    # Return success response
    return result

def callback(channel, method, properties, body): 
    global result
    print("\nReceived an email by " + __file__)
    result = processNotification(json.loads(body))
    print()

def processNotification(body):
    friend_email = body["friend_email"]
    registered = body["registered"]

    sg = sendgrid.SendGridAPIClient(api_key=os.getenv('SENDGRID_API_KEY'))
    if registered:
        data = {
        "personalizations": [
            {
            "to": [
                {
                "email": friend_email
                }
            ],
            "subject": "Join my müse group now!"
            }
        ],
        "from": {
            "email": "muse.spotify.automation@gmail.com"
        },
        "content": [
            {
            "type": "text/html",
            "value": "Dear " + friend_email + " <br><br> Click <a href='http://localhost:5173/'>here</a> to join my müse group to customise your own <strong>spotify playlists</strong> with your friends! <br><br>Best Regards,<br>müse"
            }
        ]
        }
    else:
        data = {
        "personalizations": [
            {
            "to": [
                {
                "email": friend_email
                }
            ],
            "subject": "Join my müse group now!"
            }
        ],
        "from": {
            "email": "muse.spotify.automation@gmail.com"
        },
        "content": [
            {
            "type": "text/html",
            "value": "Dear " + friend_email + " <br><br> Click <a href='http://localhost:5173/signup'>here</a> to join my müse group to customise your own <strong>spotify playlists</strong> with your friends! <br><br>Best Regards,<br>müse"
            }
        ]
        }

    try:
        response = sg.client.mail.send.post(request_body=data)
        print(response.status_code)
        print(response.body)
        print(response.headers)

        return jsonify(
            {
                "code": 201,
                "message": "notification to friend sent"
            }
        ), 201

    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred while sending the notification to friend. " + str(e.message)
            }
        ), 500

@app.route("/api/v1/top_items_email", methods=['POST'])
def top_items_email():
    global result
    result = None

    amqp_setup.check_setup()
    queue_name = 'Notifications'
    amqp_setup.channel.basic_consume(queue=queue_name, on_message_callback=callback_top, auto_ack=True)
    while result is None:
        try:
            amqp_setup.connection.process_data_events(time_limit=1)
        except pika.exceptions.ConnectionClosed:
            return
        except KeyboardInterrupt:
            amqp_setup.channel.stop_consuming()
            break

    # Return success response
    return result

def callback_top(channel, method, properties, body): 
    global result
    print("\nReceived an email by " + __file__)
    result = process_top_items(json.loads(body))
    print()

def process_top_items(body):
    email = body["email"]
    top_artists = body["top_artists"]
    top_tracks = body["top_tracks"]

    sg = sendgrid.SendGridAPIClient(api_key=os.getenv('SENDGRID_API_KEY'))
    data = {
    "personalizations": [
        {
        "to": [
            {
            "email": email
            }
        ],
        "subject": "Your Top Artists and Tracks!"
        }
    ],
    "from": {
        "email": "muse.spotify.automation@gmail.com"
    },
    "content": [
        {
        "type": "text/html",
        "value": f"Dear {email}, here are your top artists and tracks as requested from our website, müse!<br><br> <h3>Your Top Artists:</h3><ol><li>{top_artists[0]}</li><li>{top_artists[1]}</li><li>{top_artists[2]}</li><li>{top_artists[3]}</li><li>{top_artists[4]}</li></ol><br><br> <h3>Your Top Tracks:</h3><ol><li>{top_tracks[0]}</li><li>{top_tracks[1]}</li><li>{top_tracks[2]}</li><li>{top_tracks[3]}</li><li>{top_tracks[4]}</li></ol><br><br>Click <a href='http://localhost:5173/'>here</a> to interact more with müse! <br><br>Best Regards,<br>müse"
        }
    ]
    }

    try:
        response = sg.client.mail.send.post(request_body=data)
        print(response.status_code)
        print(response.body)
        print(response.headers)

        return jsonify(
            {
                "code": 201,
                "message": "notification of top items sent"
            }
        ), 201

    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred while sending the notification of top items. " + str(e.message)
            }
        ), 500


if __name__ == '__main__':
    print("This is flask for " + os.path.basename(__file__) + ": manage notifications ...")
    app.run(host='0.0.0.0', port=4999, debug=True)