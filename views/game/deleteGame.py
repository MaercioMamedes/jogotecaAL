from main import app, db
from flask import flash, redirect, url_for, session
from models import Games, Users
from werkzeug.exceptions import NotFound
import os
from helpers import delete_image


"""View para deletar jogo do Banco de dados"""
@app.route('/deletar/<int:id_game>')
def delete_game(id_game):
    user_nickname = session['user_logged']

    try:
        user = Users.query.filter_by(nickname=user_nickname).first_or_404()
        if user.is_adm:
            game = Games.query.filter_by(id=id_game)
            url_game = game.first_or_404().url_image
            game.delete()
            delete_image(url_game)
            db.session.add(user)

    except NotFound:
        flash('Exclusão de Jogo não realizda','danger')
        return redirect(url_for('index'))

    except FileNotFoundError as err:
        print(err, 'Jogo sem imagem cadastrada')

    except TypeError as err:
        print(err, 'Jogo sem imagem')
    else:
        print('Exclusão da imagem do jogo realizada com sucesso')

    db.session.commit()
    flash('Jogo deletado com sucesso', 'success')

    return redirect(url_for('index'))

