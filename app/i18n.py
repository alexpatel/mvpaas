# -*- coding: UTF-8 -*-
"""
BoGO: Flask-Babel integration

The default I18N configuration provided here is fairly useless (and harmless)
See: https://pythonhosted.org/Flask-Babel/

Copyright 2017, Anonymous Author
License: MIT
"""
from flask.ext.babel import Babel

def get_locale():
    return 'en'

def init_app(app):
    babel = Babel(app)
    babel.localeselector(get_locale)
