from flask_restful import Api
from app import flask_app

flask_api = Api(flask_app)

from api.v1.routes import flask_api
