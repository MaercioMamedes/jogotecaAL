from main import app, db
from flask import redirect, url_for, render_template, request
from models import Users, Games


@app.route('/atualizar-jogo/<int:id_game>', methods=['POST','GET'])
def update_game(id_game):
    if request.method == 'GET':
        game = Games.query.filter_by(id=id_game).first_or_404()
        print(game)
        return render_template('games/updateGame.html', title='Atualizando o Jogo', game=game)

    elif request.method == 'POST':
        game = Games.query.filter_by(id=id_game).first_or_404()
        name = request.form['name']
        category = request.form['category']
        console = request.form['console']

        game.name = name
        game.category = category
        game.console = console

        db.session.add(game)
        db.session.commit()

        return redirect(url_for('my_games'))
