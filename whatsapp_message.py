"""
This module sends a message via whatsapp to designated recipients.
Twilio Whatsapp sandbox is being used to send the messages
"""

import os
import json
import emoji
from twilio.rest import Client


def send_whatsapp_msg(event=None, context=None):

    # These values have been set on the AWD Lambda console
    account_sid = os.environ["account_sid"]
    auth_token = os.environ["auth_token"]

    # Create the Twilio client object
    client = Client(account_sid, auth_token)

    # Read the names and phone numbers from the directory.json file
    with open("directory.json", "r") as f:
        recipients = json.load(f)

    for recipient in recipients["members"]:
        message = client.messages.create(
            body=f'Good Morning, {recipient["name"]}! {emoji.emojize(":smiling_face:")}',
            from_="whatsapp:+14155238886",
            to=f'whatsapp:{recipient["phone"]}',
        )
