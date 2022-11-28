from main import app, db
from models import Games, Users
from flask import session, redirect, render_template, url_for, request
from datetime import datetime


@app.route('/novo-jogo', methods=['POST', 'GET'])
def new_game():
    if request.method == 'GET':
        if 'user_logged' in session and session['user_logged'] is not None:
            return render_template('games/newGame.html')
        else:
            return redirect(url_for('login', next_page='new_game'))

    elif request.method == 'POST':
        # user identification
        username = session['user_logged']
        user = Users.query.filter_by(nickname=username).first()

        # game identification
        name = request.form['name']
        category = request.form['category']
        console = request.form['console']
        creted_by = user.name
        created = datetime.now()

        game = Games(name=name, category=category, console=console, created_by=creted_by, created_on=created)

        db.session.add(game)
        user.add_game(game)
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('index'))

    else:
        raise Exception('erro')
