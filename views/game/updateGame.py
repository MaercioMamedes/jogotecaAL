from main import app, db
from flask import redirect, url_for, render_template, request
from models import Games
from helpers import delete_image
from forms.gameForm import GameForm
import time


"""View para atualizar dados dos Jogos cadastrados"""
@app.route('/atualizar-jogo/<int:id_game>', methods=['POST','GET'])
def update_game(id_game):
    if request.method == 'GET':
        game = Games.query.filter_by(id=id_game).first_or_404() #tratar erro
        form = GameForm()
        form.name.data = game.name
        form.category.data = game.category
        form.console.data = game.console


        return render_template('games/updateGame.html', title='Atualizando o Jogo', game=game, form=form)

    elif request.method == 'POST':
        # game identification

        game = Games.query.filter_by(id=id_game).first_or_404()
        name = request.form['name']
        category = request.form['category']
        console = request.form['console']

        # remove old image
        if game.url_image is not None:
            delete_image(game.url_image)

        # save new image
        image_game = request.files['image']
        upload_path = app.config['UPLOAD_PATH']
        url_image = f'{upload_path}/game/capa-{game.id}-{time.time()}.jpg'
        image_game.save(url_image)

        # update data game
        game.name = name
        game.category = category
        game.console = console
        game.url_image = url_image

        # save in database
        db.session.add(game)
        db.session.commit()

        return redirect(url_for('my_games'))
