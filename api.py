from flask import Flask
from redis import Redis
import os

db = os.environ['DB_SERVICE_SERVICE_HOST']
app = Flask(__name__)
redis = Redis(db, port=6379)

@app.route('/')
def hello():
    return 'Hi guuys'

@app.route('/health')
def health():
    redis.ping() 
    return 'I'm fine', 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)