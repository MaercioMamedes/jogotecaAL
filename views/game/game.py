from main import app
from models import Games
from flask import render_template


@app.route('/game/<int:id_game>')
def game(id_game):
    game = Games.query.filter_by(id=id_game).first_or_404()
    return render_template('games/game.html', game=game)
