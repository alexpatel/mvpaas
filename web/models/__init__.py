# -*- coding: UTF-8 
"""
BoGO: Flask-SQLAlchemy models
"""
from app.db import db

from user import User


# Create database
def init_db_tables(app):
    with app.app_context():
        db.create_all()


# Initialize core db data
def init_db_data(app):
    from werkzeug.security import generate_password_hash

    with app.app_context():
        u_admin = User(id = 0, email='admin@test.com', password=generate_password_hash('admin'))
        u_test = User(id = 1, email='test@test.com', password=generate_password_hash('test'))
        db.session.add(u_admin)
        db.session.add(u_test)
        db.session.commit()


