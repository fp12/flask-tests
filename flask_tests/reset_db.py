from app import app, init_app
from database import reset_database


init_app(app)
app.app_context().push()
reset_database()
