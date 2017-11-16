from flask_restful import reqparse

from app import cache
import mlmodels.predictors


def init_request_parser(predictor):
    parser = reqparse.RequestParser(bundle_errors=True)

    for column_name, column_type in predictor.get_column_types().items():
        if column_name != predictor.prediction_field:
            parser.add_argument(
                column_name,
                type=column_type,
                required=True,
                location='json'
            )

    return parser


@cache.memoize()
def get_predictor(name, version):
    klass_name = snake_to_camel(name)
    predictor_klass = getattr(mlmodels.predictors, klass_name)

    predictor = predictor_klass(version=version)
    predictor.load()

    print(f'{klass_name} v{version} loaded')

    return predictor


def snake_to_camel(input_text):
    return ''.join(x.capitalize() for x in input_text.split('_'))
