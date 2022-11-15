from main import app
from models import *
from flask import render_template


@app.route('/')
def index():
    list_game = Games.query.order_by(Games.id)
    return render_template('index.html', title='Jogos', games=list_game)
