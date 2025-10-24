from flask import Flask, render_template, request
from flask_mail import Mail, Message
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)

# Email configuration (pulled from environment variables)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')

mail = Mail(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    msg = Message(
        subject=f"New message from {name}",
        sender=app.config['MAIL_USERNAME'],  # safer to use your verified sender
        recipients=[app.config['MAIL_USERNAME']],
        body=f"From: {name} <{email}>\n\n{message}"
    )
    mail.send(msg)
    return render_template('index.html', success=True)

if __name__ == '__main__':
    app.run(debug=True)