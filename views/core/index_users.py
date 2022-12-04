from main import app
from flask import render_template
from models.users import *


"""View responsável por exibir informações sobre os usuários cadastrados"""
@app.route('/usuarios')
def index_users():
    users = Users.query.all()
    return render_template('core/indexUsers.html', title='Usuários Cadastrados', users=users)
