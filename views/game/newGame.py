from main import app, db
from models import Games, Users
from flask import session, redirect, render_template, url_for, request
from forms.gameForm import GameForm
from datetime import datetime
import time


"""View para cadastrar um novo jogo"""
@app.route('/novo-jogo', methods=['POST', 'GET'])
def new_game():
    if request.method == 'GET':
        if 'user_logged' in session and session['user_logged'] is not None:
            form = GameForm()
            return render_template('games/newGame.html', title='Novo Jogo', form=form)
        else:
            return redirect(url_for('login', next_page='new_game'))

    elif request.method == 'POST':


        # user identification

        username = session['user_logged']
        user = Users.query.filter_by(nickname=username).first()

        # game identification
        form = GameForm(request.form)

        name = form.name.data
        category = form.category.data
        console = form.category.data
        creted_by = user.name
        created = datetime.now()

        # create Game
        game = Games(name=name, category=category, console=console, created_by=creted_by, created_on=created)

        # Save game and User in Data Base
        db.session.add(game)
        user.add_game(game)
        db.session.add(user)
        db.session.commit()

        # Upload of the image to Application
        image_game = request.files['image']
        upload_path = app.config['UPLOAD_PATH']
        url_image = f'{upload_path}/game/capa-{game.id}-{time.time()}.jpg'
        image_game.save(url_image)

        # save url image in to Data Base
        game.url_image = url_image
        db.session.add(game)
        db.session.commit()

        return redirect(url_for('index'))

    else:
        raise Exception('erro')
