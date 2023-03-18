#!/usr/bin/env python3
# The above shebang (#!) operator tells Unix-like environments
# to run this file as a python3 script

import os
from flask import Flask, request, jsonify
import sendgrid
from sendgrid.helpers.mail import Mail
import requests
# importing twilio
import twilio
from twilio.rest import Client

# for SendGrid
API_KEY = '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'

# for twilio
account_sid = 'ACb659e2c670af156d9331b323e2d15324'
auth_token = '0de7a8f775950e4b2411b3da961d814c'

app = Flask(__name__)


@app.route("/notify/email", methods=['POST'])
def create_email():
    user_email = request.json.get('user_email', None)

    message = Mail(
        from_email = 'muse.spotify.automation@gmail.com',
        to_emails = user_email,
        subject = 'Join my müse group now!',
        html_content = "Dear User, <br><br> Click <a href='google.com'>here</a> to join my müse group to customise your own <strong>spotify playlists</strong> with your friends! <br><br>Best Regards,<br>müse")

    try:
        sg = sendgrid.SendGridAPIClient(API_KEY)
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)

    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred while sending the notification. " + str(e.message)
            }
        ), 500

    return jsonify(
        {
            "code": 201,
            "response": "notification sent"
        }
    ), 201


@app.route("/notify/message", methods=['POST'])
def create_whatsapp():
    message_body = request.json.get('message_body', None)
    recipient = request.json.get('recipient_number', None)

    # try:
    client = Client(account_sid, auth_token)
    ''' Change the value of 'from' with the number 
    received from Twilio and the value of 'to'
    with the number in which you want to send message.'''
    message = client.messages.create(
                                from_= '+15075017250',
                                body = message_body,
                                to = recipient
                            )
    
    print(message.sid)

    # except twilio.TwilioRestException as e:
    #     return jsonify(
    #         {
    #             "code": 500,
    #             "message": "An error occurred while sending the notification. " + str(e)
    #         }
    #     ), 500

    return jsonify(
        {
            "code": 201,
            "response": "notification sent"
        }
    ), 201

if __name__ == '__main__':
    print("This is flask for " + os.path.basename(__file__) + ": manage notifications ...")
    app.run(host='0.0.0.0', debug=True)