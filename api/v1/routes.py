from flask_restful import Resource

from api import flask_api

API_VERSION = 'v1'
ROUTE_PREFIX = f'/api/{API_VERSION}'


class Heartbeat(Resource):
    def get(self):
        return {
            'api_version': API_VERSION,
            'status': 'success'
        }, 200

flask_api.add_resource(Heartbeat, f'{ROUTE_PREFIX}/heartbeat', endpoint='api.v1.heartbeat')
