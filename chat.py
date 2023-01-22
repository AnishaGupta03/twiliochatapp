# importing twilio
from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com / console
account_sid = 'AC97f5ac2c9662ca98ee680e20fd70015b'
auth_token = 'a268a3e361a6293dacb5efe2c7896904'

client = Client(account_sid, auth_token)

''' Change the value of 'from' with the number
received from Twilio and the value of 'to'
with the number in which you want to send message.'''
message = client.messages.create(
							from_='+918252071214',
							body ='hello, how are you?',
							to ='+916204788657'
						)

print(message.sid)
