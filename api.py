#Imports
from flask import Flask
from redis import Redis
import os

#   REST API that says hello and checks DB status

db = os.environ['DB_SERVICE_SERVICE_HOST']
app = Flask(__name__)
redis = Redis(db, port=6379)

#This functions binds an URL to a function
#GET function that returns a string with 'Hi Guys'
@app.route('/')
def hello():
    return 'Hi guuys'

#GET function. This functions checks the health of the Redis DB by mean of a ping status
@app.route('/health')
def health():
    redis.ping() 
    return 'I am fine', 200

#Runs the app. Main method
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)