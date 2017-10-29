from flask import Flask, redirect, url_for
from flask_appconfig import AppConfig
from flask_bootstrap import Bootstrap

from rest import blueprint as rest_api
from bootstrap import blueprint as boostrap_bp
from pure import blueprint as pure_bp
from bootstrap.nav import nav

from debug import debug_init


if __name__ == '__main__':
    app = Flask(__name__)
    app.register_blueprint(rest_api, url_prefix='/api/v1')
    app.register_blueprint(boostrap_bp, url_prefix='/bootstrap')
    app.register_blueprint(pure_bp, url_prefix='/pure')

    nav.init_app(app)
    AppConfig(app, None)
    Bootstrap(app)

    debug_init(app)

    @app.route('/')
    def index():
        return redirect(url_for('bootstrap_.index'))

    app.run(debug=True)
