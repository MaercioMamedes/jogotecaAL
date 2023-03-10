from main import app
from flask import render_template, request, flash, redirect, url_for
from models import *
from forms.loginForm import LoginForm


"""View de Login"""
@app.route('/login')
def login():
    form = LoginForm()
    next_page = request.args.get('next_page')
    return render_template('core/login.html', next_page=next_page, title='Faça seu login', form=form)
