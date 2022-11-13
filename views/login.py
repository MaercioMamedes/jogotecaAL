from main import app
from flask import render_template, request


@app.route('/login')
def login():
    next_page = request.args.get('next-page')
    return render_template('login.html', next_page=next_page)
