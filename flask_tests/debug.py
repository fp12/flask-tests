from flask_debugtoolbar import DebugToolbarExtension


def setup(app):
    app.config['SECRET_KEY'] = 'not so secret'
    DebugToolbarExtension(app)
