from flask import Blueprint


blueprint = Blueprint('pure', __name__)


@blueprint.route('/')
def index():
    return 'Pure page'
