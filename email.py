import smtplib
import ssl
from email.message import EmailMessage


EMAIL = "your_email@gmail.com"
APP_PASSWORD = "your_16_digit_app_password"


receiver = "receiver_email@gmail.com"
subject = "Automated Email from Python"
body = """Hello!
This email is sent automatically using Python.
Have a great day 🚀"""


msg = EmailMessage()
msg["From"] = EMAIL
msg["To"] = receiver
msg["Subject"] = subject
msg.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    smtp.login(EMAIL, APP_PASSWORD)
    smtp.send_message(msg)

print("✅ Email sent successfully!")
