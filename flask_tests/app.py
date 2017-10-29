from flask import Flask

from rest import api


app = Flask(__name__)
api.init_app(app)


@app.route('/')
def home():
    return 'Flask tests'


if __name__ == '__main__':
    app.run(debug=True)
