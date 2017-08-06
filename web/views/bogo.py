
from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

bogo = Blueprint('bogo', __name__,
                 template_folder='templates')

@simple_page.route('/', defaults={'page': 'index'})
@simple_page.route('/<page>')
def show(page):
    try:
        return render_template('bogo/%s.html' % page)
    except TemplateNotFound:
        abort(404)
