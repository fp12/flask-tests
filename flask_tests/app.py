from flask import Flask, redirect, url_for
from flask_appconfig import AppConfig

from rest import blueprint as rest_api
from bootstrap import setup as bootstrap_setup, blueprint as boostrap_bp
from pure import setup as pure_setup, blueprint as pure_bp

from debug import setup as debug_setup


if __name__ == '__main__':
    app = Flask(__name__)
    AppConfig(app, None)
    bootstrap_setup(app)
    pure_setup(app)
    debug_setup(app)

    app.register_blueprint(rest_api, url_prefix='/api/v1')
    app.register_blueprint(boostrap_bp, url_prefix='/bootstrap')
    app.register_blueprint(pure_bp, url_prefix='/pure')

    @app.route('/')
    def index():
        return redirect(url_for('bootstrap_demo.index'))

    app.run(debug=True)
