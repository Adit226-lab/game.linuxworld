from twilio.rest import Client

ACCOUNT_SID = "your_account_sid_here"
AUTH_TOKEN = "your_auth_token_here"
TWILIO_SMS_NUMBER = "your_twilio_phone_here"

client = Client(ACCOUNT_SID, AUTH_TOKEN)

message = client.messages.create(
    body="Hello! This SMS was sent using Python automation 🚀",
    from_=TWILIO_SMS_NUMBER,
    to="receiver_number_here"
)

print("✅ Message sent successfully! SID:", message.sid)
