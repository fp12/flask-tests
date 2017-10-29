from flask_restplus import Api
from .items import api as api_items


api = Api(
    title='Flask Tests API',
    version='1.0',
    description='Just some tests',
    endpoint='wtf'
)

base = 'api'
version = 'v1'

base_route = f'/{base}/{version}'

api.add_namespace(api_items, path=f'{base_route}/items')
