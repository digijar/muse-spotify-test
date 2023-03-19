# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python

API_KEY = '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'

import sendgrid
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email='muse.spotify.automation@gmail.com',
    to_emails='jaronchan123@gmail.com',
    subject='Join my müse group now!',
    html_content="Dear User, <br><br> Click <a href='google.com'>here</a> to join my müse group to customise your own <strong>spotify playlists</strong> with your friends! <br><br>Best Regards,<br>müse")
try:
    sg = sendgrid.SendGridAPIClient(API_KEY)
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message) 