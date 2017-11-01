from flask import jsonify, make_response
from flask_restful import Resource

from api import flask_api
from api.helpers import init_request_parser, get_predictor

API_VERSION = 1
ROUTE_PREFIX = f'/api/v{API_VERSION}'


class Heartbeat(Resource):
    def get(self):
        return make_response(jsonify({'status': 'ok'}), 200)


class Predictor(Resource):
    def get(self, predictor_name):
        try:
            predictor = get_predictor(predictor_name, API_VERSION)
        except AttributeError:
            return make_response(jsonify({'message': f'{predictor_name} not found'}), 404)

        parser = init_request_parser(predictor)
        parsed_args = parser.parse_args(strict=True)
        result = predictor.predict(parsed_args)

        return make_response(
            jsonify({
                'field': predictor.prediction_field,
                'result': result,
                'version': predictor.clf_version
            }), 200
        )

flask_api.add_resource(Heartbeat, f'{ROUTE_PREFIX}/heartbeat', endpoint=f'api.v{API_VERSION}.heartbeat')

flask_api.add_resource(
    Predictor,
    f'{ROUTE_PREFIX}/predict/<string:predictor_name>',
    endpoint=f'api.v{API_VERSION}.predict'
)
