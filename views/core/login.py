from main import app
from flask import render_template, request, flash, redirect, url_for
from models import *


@app.route('/login')
def login():
    next_page = request.args.get('next_page')
    return render_template('core/login.html', next_page=next_page)
