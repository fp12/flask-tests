from flask import Flask

from rest import blueprint as api


app = Flask(__name__)
app.register_blueprint(api, url_prefix='/api/v1')


@app.route('/')
def home():
    return 'Flask tests'


if __name__ == '__main__':
    app.run(debug=True)
