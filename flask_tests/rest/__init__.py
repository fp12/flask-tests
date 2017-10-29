from flask import Blueprint
from flask_restplus import Api

from .items import api as api_items

blueprint = Blueprint('api', __name__)

_api = Api(
    blueprint,
    title='Flask Tests API',
    version='1.0',
    description='Just some tests'
)

_api.add_namespace(api_items, path=f'/items')
