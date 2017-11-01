from flask import Flask
from flask_caching import Cache
from dotenv import load_dotenv, find_dotenv

# load environment variables
load_dotenv(find_dotenv())

flask_app = Flask(__name__)
cache = Cache(flask_app, config={'CACHE_TYPE': 'simple'})

from api import flask_app
