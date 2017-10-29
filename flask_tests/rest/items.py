from flask_restplus import Resource

from rest.base import api, base_route


@api.route(f'{base_route}/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}
