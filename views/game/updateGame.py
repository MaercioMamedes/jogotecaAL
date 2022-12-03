from main import app, db
from flask import redirect, url_for, render_template, request
from models import Users, Games
from helpers import delete_image
import time


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

        if game.url_image is not None:
            delete_image(game.url_image)

        image_game = request.files['image']
        upload_path = app.config['UPLOAD_PATH']
        url_image = f'{upload_path}/capa-{game.id}-{time.time()}.jpg'
        image_game.save(url_image)

        game.name = name
        game.category = category
        game.console = console
        game.url_image = url_image

        db.session.add(game)
        db.session.commit()

        return redirect(url_for('my_games'))
