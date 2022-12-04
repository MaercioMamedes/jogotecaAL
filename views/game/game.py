from main import app
from models import Games
from flask import render_template


"""View para exibir dados de jogo cadastrado"""
@app.route('/game/<int:id_game>')
def game(id_game):
    game_data = Games.query.filter_by(id=id_game).first_or_404()
    return render_template('games/game.html', game=game_data)
