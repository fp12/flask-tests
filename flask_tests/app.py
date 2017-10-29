from flask import Flask, redirect, url_for
from flask_bootstrap import Bootstrap

from rest import blueprint as rest_api
from bootstrap import blueprint as boostrap_bp
from pure import blueprint as pure_bp

from bootstrap.nav import nav


app = Flask(__name__)
app.register_blueprint(rest_api, url_prefix='/api/v1')
app.register_blueprint(boostrap_bp, url_prefix='/bootstrap')
app.register_blueprint(pure_bp, url_prefix='/pure')


# @app.route('/')
# def index():
#     return redirect(url_for('bootstrap_.index'))


if __name__ == '__main__':
    nav.init_app(app)
    Bootstrap(app)
    app.run(debug=True)
