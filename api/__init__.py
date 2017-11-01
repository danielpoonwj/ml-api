from flask_restful import Api
from app import flask_app

flask_api = Api(flask_app)

from api.v1.routes import flask_api

from api.helpers import get_predictor

# cache predictor prefork
get_predictor('wine_quality', 1)
