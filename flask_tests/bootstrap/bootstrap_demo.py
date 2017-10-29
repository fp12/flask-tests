from flask import Blueprint, render_template
from flask_bootstrap import Bootstrap

from .nav import nav

blueprint = Blueprint('bootstrap_demo', __name__, template_folder='templates')


def setup(app):
    Bootstrap(app)
    nav.init_app(app)


@blueprint.route('/')
def index():
    return render_template('index.jinja')
