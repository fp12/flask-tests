from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
from . import item  # noqa


def reset_database():
    db.drop_all()
    db.create_all()
