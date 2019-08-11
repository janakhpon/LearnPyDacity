from twilio.rest import Client

account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Hey there, twilio is working fine and it's awesome",
                     from_='+',
                     to='+'
                 )

print(message.sid)
