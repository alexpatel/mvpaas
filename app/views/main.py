# -*- coding: UTF-8 -*-
"""
BoGO: Main views
"""
from flask import Blueprint, render_template, flash
blueprint = Blueprint('main', __name__, url_prefix='')
from flask.ext.login import login_required

@blueprint.route('/')
@login_required
def index():
    return render_template('index.html')
