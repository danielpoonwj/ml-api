from flask_restful import Resource, reqparse

from api import flask_api
from app import cache

from mlmodels.predictors import WineQuality

API_VERSION = 'v1'
ROUTE_PREFIX = f'/api/{API_VERSION}'


class Heartbeat(Resource):
    def get(self):
        return {
            'status': 'ok'
        }


class WineQualityResource(Resource):
    def get(self):
        predictor = get_predictor()

        parser = reqparse.RequestParser(bundle_errors=True)
        for column_name, column_type in predictor.get_column_types().items():
            if column_name != predictor.prediction_field:
                parser.add_argument(
                    column_name,
                    type=column_type,
                    required=True,
                    location='args'
                )

        parsed_args = parser.parse_args(strict=True)
        result = predictor.predict(parsed_args)

        return {
            'field': predictor.prediction_field,
            'result': result,
            'version': predictor.clf_version
        }


@cache.cached(key_prefix='wine_quality')
def get_predictor():
    predictor = WineQuality(version=1)
    predictor.load()
    return predictor

flask_api.add_resource(Heartbeat, f'{ROUTE_PREFIX}/heartbeat', endpoint='api.v1.heartbeat')
flask_api.add_resource(WineQualityResource, f'{ROUTE_PREFIX}/predict/wine_quality', endpoint='api.v1.predict.wine_quality')
