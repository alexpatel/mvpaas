from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()
Base = db.Model

def init_app(app):
    db.init_app(app)
