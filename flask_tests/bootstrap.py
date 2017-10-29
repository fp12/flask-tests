from flask import Blueprint

blueprint = Blueprint('bootstrap', __name__)


@blueprint.route('/')
def index():
    return 'Bootstrap page'
