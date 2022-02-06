from flask import Flask
from flask_mail import Mail, Message
from flask_wtf.csrf import CSRFProtect
from routes import backend, home
import os

SECRET_KEY = os.urandom(32)

csrf = CSRFProtect()

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
app.register_blueprint(backend)
app.register_blueprint(home)

csrf.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)


app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'amwarkow@gmail.com'
app.config['MAIL_PASSWORD'] = '*****'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@home.route('/process_email', methods=['POST'])
def process_email():
    msg = Message('Test', recipients=['aw3334@drexel.edu'])
    msg.body = 'This is a test email' #Customize based on user input
    mail.send(msg)

    return 'done'
