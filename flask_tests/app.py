from flask import Flask, redirect, url_for

from rest import blueprint as rest_api
from bootstrap import blueprint as boostrap_bp
from pure import blueprint as pure_bp


app = Flask(__name__)
app.register_blueprint(rest_api, url_prefix='/api/v1')
app.register_blueprint(boostrap_bp, url_prefix='/bootstrap')
app.register_blueprint(pure_bp, url_prefix='/pure')


@app.route('/')
def index():
    return redirect(url_for('bootstrap.index'))


if __name__ == '__main__':
    app.run(debug=True)
