from main import app, db
from models.users import Users
from models.games import Games
from flask import session, redirect, url_for


"""View responsável por remover jogo do portfólio do usuário"""
# Rever arquitetura dessa view
@app.route('/remover-jogo/<int:id_game>')
def remove_game_from_portfolio(id_game):
    try:
        game = Games.query.filter_by(id=id_game).first_or_404()
        user = Users.query.filter_by(nickname=session['user_logged']).first_or_404()

        user.remove_game(game)
        db.session.add(user)
        db.session.commit()
        
        return redirect(url_for('my_games'))

    except: # tratar melhor essa exceção
        print("Jogo não encontrado")
        return redirect(url_for('index'))
