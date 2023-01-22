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

message = client.conversations \
                .v1 \
                .conversations('CH105027da860c4d548371f1ad4b0fde70') \
                .messages('IMf305bc653c81489994a3a749b025b4d5') \
                .update(author='Abhishek', body='I take back what I said')

print(message.conversation_sid)
print(message.author)
print(message.body)