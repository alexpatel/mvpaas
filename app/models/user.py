# -*- coding: UTF-8 
from sqlalchemy import *
from flask.ext.login import UserMixin

from app.db import Base


class User(Base, UserMixin):
    id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=True)
    password = Column(String(64))


