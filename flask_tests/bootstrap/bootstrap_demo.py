from flask import Blueprint, render_template


blueprint = Blueprint('bootstrap_demo', __name__, template_folder='templates')


@blueprint.route('/')
def index():
    return render_template('index.jinja')
