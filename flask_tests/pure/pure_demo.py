from flask import Blueprint, render_template
from flask_pure import Pure


blueprint = Blueprint('pure_demo', __name__, template_folder='templates')


def setup(app):
    Pure(app)


@blueprint.route('/')
def index():
    return render_template('hello.jinja')
