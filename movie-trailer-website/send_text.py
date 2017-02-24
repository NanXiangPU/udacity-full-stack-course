from twilio.rest import TwilioRestClient


account_sid = "AC848b7fee169985345c5b84210e46b26b"
auth_token = "33bc05e5a813e49e1a8d2ecd0a606e96"

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Saonimabi",
    to="+17654795778",
    from_="+12103615823")

print(message.sid)