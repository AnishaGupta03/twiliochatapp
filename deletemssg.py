# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')


client = Client(account_sid, auth_token)

client.conversations.v1.conversations('CH105027da860c4d548371f1ad4b0fde70') \
                       .messages('IMc10b5631a35e4f80a461eecb243465c7') \
                       .delete()
