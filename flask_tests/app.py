from flask import Flask, redirect, url_for
from flask_appconfig import AppConfig

from database import db
from rest import blueprint as rest_api
from bootstrap import setup as bootstrap_setup, blueprint as boostrap_bp
from pure import setup as pure_setup, blueprint as pure_bp
from debug import setup as debug_setup


sqlite_file = 'db.sqlite'
app = Flask(__name__)


def init_app(app):
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + sqlite_file
    AppConfig(app, None)

    bootstrap_setup(app)
    pure_setup(app)

    db.init_app(app)

    debug_setup(app)

    app.register_blueprint(rest_api, url_prefix='/api/v1')
    app.register_blueprint(boostrap_bp, url_prefix='/bootstrap')
    app.register_blueprint(pure_bp, url_prefix='/pure')

    @app.route('/')
    def index():
        return redirect(url_for('bootstrap_demo.index'))


if __name__ == '__main__':
    init_app(app)
    app.run(debug=True)
