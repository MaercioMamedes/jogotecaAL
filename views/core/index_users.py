from main import app
from flask import render_template
from models.users import *


@app.route('/usuarios')
def index_users():
    users = Users.query.all()
    return render_template('core/indexUsers.html', users=users)
