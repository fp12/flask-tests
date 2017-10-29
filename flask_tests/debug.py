from flask_debugtoolbar import DebugToolbarExtension


def debug_init(app):
    app.config['SECRET_KEY'] = 'not so secret'
    DebugToolbarExtension(app)
