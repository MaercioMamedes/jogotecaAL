from main import app
from flask import render_template, session, redirect, url_for
from models import Users


"""View responsável por exibir jogos cadastrados no portfólio do usuário"""
@app.route('/meus-jogos')
def my_games():
    if 'user_logged' in session and session['user_logged'] is not None:
        username = session['user_logged']
        user = Users.query.filter_by(nickname=username).first_or_404()

        list_games = user.games
        print(list_games)

        return render_template('core/myGames.html', games=list_games)
    else:
        return redirect(url_for('login', next_page='my_games'))
