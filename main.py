from flask import Flask
from init import db
import os



app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'