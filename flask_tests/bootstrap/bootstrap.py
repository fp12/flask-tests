from flask import Blueprint, render_template

# from .nav import nav


# '_' is added to not conflict with Bootstrap extension
blueprint = Blueprint('bootstrap_', __name__, template_folder='templates')


@blueprint.route('/')
def index():
    return render_template('index.jinja')
