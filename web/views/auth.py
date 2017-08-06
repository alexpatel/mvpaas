# -*- coding: UTF-8 -*-
"""
BoGO: Flask-Login integration
"""
from flask import Blueprint, render_template, flash, redirect, request, url_for, current_app
from flask.ext.login import LoginManager, login_user, logout_user, login_required, current_user
from flask_wtf import Form
from wtforms import fields, validators
from werkzeug.security import check_password_hash

from app.db import db
from app.models import User

blueprint = Blueprint('auth', __name__, url_prefix='')


def init_blueprint(setup_state):
    '''Set up Flask-Login on blueprint registration'''
    
    app = setup_state.app
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_message_category = "info"
    login_manager.login_view = 'auth.login'
    login_manager.login_message = None


    # Create user loader function
    @login_manager.user_loader
    def load_user(user_id):
        return db.session.query(User).get(user_id)

blueprint.record_once(init_blueprint)



@blueprint.route("/login", methods=["GET", "POST"])
def login():

    if request.method == 'POST':

        email = request.form['email']
        password = request.form['password']        
        user = db.session.query(User).filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(request.args.get("next") or url_for("main.index"))
        else:
            flash("Invalid credentials.", 'error')
            return render_template("login.html")
    else:
        return render_template("login.html")


@blueprint.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have logged out.")
    return redirect(url_for("main.index"))


@blueprint.route("/account")
@login_required
def account():
    return render_template("account.html", user=current_user)
