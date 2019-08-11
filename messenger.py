from twilio.rest import Client

account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Twilio is here",
                     from_='+',
                     to='+'
                 )

print(message.sid)
