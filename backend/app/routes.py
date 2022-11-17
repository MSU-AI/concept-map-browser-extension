from flask import Blueprint, request, render_template, session

import random

routes = Blueprint("routes", __name__)

@routes.route("/")
def index():
    text = request.args.get('text')
    if text != None:
        session['i'] = text
    if 'i' in session:
        text = session['i']
    return render_template('sample_network.html', value=text)
