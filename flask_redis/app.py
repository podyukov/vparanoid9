import time
import redis
import socket
from flask import Flask

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

def get_hit_count():
    return cache.incr('hits')

@app.route('/')
def hello():
    count = get_hit_count()
    return 'Hello World version 5.0! I have been seen {} times. My name is: {}'.format(count, socket.gethostname())
