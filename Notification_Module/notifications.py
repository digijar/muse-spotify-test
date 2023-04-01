# all imports
import os
import json
from flask import Flask, request, jsonify
import sendgrid
from sendgrid.helpers.mail import *
import requests
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

    sg = sendgrid.SendGridAPIClient(api_key=os.getenv('SENDGRID_API_KEY'))
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

    try:
        response = sg.client.mail.send.post(request_body=data)
        print(response.status_code)
        print(response.body)
        print(response.headers)

        return jsonify(
            {
                "code": 201,
                "message": "notification sent"
            }
        ), 201

    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred while sending the notification. " + str(e.message)
            }
        ), 500

    # return jsonify(
    #     {
    #         "code": 201,
    #         "message": "notification sent"
    #     }
    # ), 201

    # try:
    #     print(json.dumps(message.get(), sort_keys=True, indent=4))
    #     return message.get()

    # except SendGridException as e:
    #     print(e.message)


# def create_email():
#     user_email = request.json.get('user_email', None)

#     message = Mail(
#         from_email = 'muse.spotify.automation@gmail.com',
#         to_emails = user_email,
#         subject = 'Join my müse group now!',
#         html_content = "Dear User, <br><br> Click <a href='google.com'>here</a> to join my müse group to customise your own <strong>spotify playlists</strong> with your friends! <br><br>Best Regards,<br>müse")

#     try:
#         sg = sendgrid.SendGridAPIClient(API_KEY)
#         response = sg.send(message)
#         print(response.status_code)
#         print(response.body)
#         print(response.headers)

#     except Exception as e:
#         return jsonify(
#             {
#                 "code": 500,
#                 "message": "An error occurred while sending the notification. " + str(e.message)
#             }
#         ), 500

#     return jsonify(
#         {
#             "code": 201,
#             "response": "notification sent"
#         }
#     ), 201


# @app.route("/api/v1/notify/sms", methods=['POST'])
# def create_sms():
#     message_body = request.json.get('message_body', None)
#     recipient = request.json.get('recipient_number', None)

#     # try:
#     client = Client(account_sid, auth_token)
#     ''' Change the value of 'from' with the number 
#     received from Twilio and the value of 'to'
#     with the number in which you want to send message.'''
#     message = client.messages.create(
#                                 from_= '+15075017250',
#                                 body = message_body,
#                                 to = recipient
#                             )
    
#     print(message.sid)

#     # except twilio.TwilioRestException as e:
#     #     return jsonify(
#     #         {
#     #             "code": 500,
#     #             "message": "An error occurred while sending the notification. " + str(e)
#     #         }
#     #     ), 500

#     return jsonify(
#         {
#             "code": 201,
#             "response": "notification sent"
#         }
#     ), 201

if __name__ == '__main__':
    print("This is flask for " + os.path.basename(__file__) + ": manage notifications ...")
    app.run(host='0.0.0.0', port=4999, debug=True)