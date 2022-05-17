from flask import render_template
from flask_mail import Mail, Message

mail = Mail()

def send_email(subject, recipients = []):
    msg = Message(subject,
                  sender="ljavierrodriguez@gmail.com",
                  recipients=recipients)

    msg.email = render_template('email.html')
    mail.send(msg)