# -*- coding: UTF-8 -*-
"""
BoGO: Flask-Script manager script

See: http://flask-script.readthedocs.org/

Copyright 2017, Anonymous Author
License: MIT
"""
import logging
from flask.ext.script import Manager
from app.app import create_app


app = create_app()
manager = Manager(app)


@manager.shell
def shell_context():
    from app import model
    return dict(app=app, model=model, db=model.db)


@manager.command
def runserver(log_config=None):
    'Launch a debug server.'
    if log_config is not None:
        logging.config.fileConfig(log_config)
    else:
        logging.basicConfig(level=logging.DEBUG)
    app.run(host=app.config['DEBUG_SERVER_HOST'],
            port=app.config['DEBUG_SERVER_PORT'])


@manager.command
def createdb():
    'Initialize a new database, creating tables and data.'
    from app.models import init_db_tables, init_db_data
    init_db_tables(app)
    init_db_data(app)


# -- Asset management -- #
#from flask.ext.assets import ManageAssets
## https://github.com/miracle2k/flask-assets/pull/78
#app.jinja_env.assets_environment.environment = app.jinja_env.assets_environment
#manager.add_command("assets", ManageAssets())

if __name__ == "__main__":
    manager.run()
