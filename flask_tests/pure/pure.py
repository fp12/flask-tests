from flask import Blueprint

print(__name__)
blueprint = Blueprint('pure', __name__)


@blueprint.route('/')
def index():
    return 'Pure page'
