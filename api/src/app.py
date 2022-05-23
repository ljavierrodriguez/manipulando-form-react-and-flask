import os
from flask import Flask, request, jsonify, render_template
from flask_migrate import Migrate
from flask_cors import CORS
from flask_mail import Mail, Message
from routes import user
from models import db
from dotenv import load_dotenv
import cloudinary


load_dotenv()


app = Flask(__name__)
app.config['DEBUG'] = True
app.config['ENV'] = 'development'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

""" 
app.config['MAIL_SERVER'] = "smtp.gmail.com"
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_DEBUG'] = True
app.config['MAIL_SUPPRESS_SEND'] = False 
"""


#mail = Mail()

db.init_app(app)
#mail.init_app(app)
Migrate(app, db)
CORS(app)


cloudinary.config( 
  cloud_name = os.environ.get('CLOUD_NAME'), 
  api_key = os.environ.get('CLOUD_API_KEY'), 
  api_secret = os.environ.get('CLOUD_API_SECRET'),
  secure = True
)

app.register_blueprint(user.api, url_prefix='/api')

""" 
@app.route('/api/send_mail')
def send_email():
    msg = Message("Prueba",
                  sender="ljavierrodriguez@gmail.com",
                  recipients="lrodriguez@4geeks.co")
    msg.html = "<b>Hola Mundo</b>"
    mail.send(msg)
    return "Mensaje Enviado" 
"""

@app.route('/')
def main():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
