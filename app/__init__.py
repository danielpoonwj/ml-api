from flask import Flask
from flask_caching import Cache
from dotenv import load_dotenv, find_dotenv

from api.helpers import get_predictor

flask_app = Flask(__name__)
cache = Cache(flask_app, config={'CACHE_TYPE': 'simple'})

# load environment variables
load_dotenv(find_dotenv())

# cache predictor prefork
get_predictor('wine_quality', 1)

from api import flask_app
