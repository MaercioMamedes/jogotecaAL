from main import app
from models.games import Games
from flask import render_template


@app.route('/')
def index():
    list_game = Games.query.order_by(Games.id)
    print(list_game)
    return render_template('index.html', title='Jogos', games=list_game)
