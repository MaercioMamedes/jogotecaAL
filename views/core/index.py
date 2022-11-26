from main import app
from models import *
from flask import render_template


"""Rota da página index, que lista todos os Jogos cadastrados"""


@app.route('/')
def index():
    list_game = Games.query.order_by(Games.id)
    return render_template('core/index.html', title='Jogos', games=list_game)
