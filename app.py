import os
from twilio.rest import Client
#from dotenv import load_dotenv
from flask import (
    Flask,
    flash, 
    render_template, 
    redirect,
    request,
    url_for,
)

#load_dotenv()
app = Flask(__name__)
app.secret_key = "ssssh don't tell anyone"

TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER')

account_sid = 'ACa25ddc420f9aa809969b283d3fb45d27' 
auth_token = '61b934a9fd66ed43e88aa673382bbe61' 
client = Client(account_sid, auth_token) 

def get_sent_messages():
    # TODO: Make this return a collection of messages that were sent from the number
    messages = []
    return messages

def send_message(to, body):
    client.messages.create( 
                            from_='whatsapp:+14155238886',  
                            body=body,      
                            to=to 
                        ) 

@app.route("/", methods=["GET"])
def index():
    messages = get_sent_messages()
    return render_template("index.html", messages=messages)

@app.route("/add-compliment", methods=["POST"])
def add_compliment():
    sender = request.values.get('sender', 'Someone')
    receiver = request.values.get('receiver', 'Someone')
    compliment = request.values.get('compliment', 'wonderful')
    to1 = request.values.get('to')
    to='whatsapp:'+to1
    body = f'{sender} says: {receiver} is {compliment}. See more compliments at {request.url_root}'
    send_message(to, body)
    flash('Your message was successfully sent')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
