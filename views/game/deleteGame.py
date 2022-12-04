from main import app, db
from flask import flash, redirect, url_for
from models import Games
import os
from helpers import delete_image


"""View para deletar jogo do Banco de dados"""
@app.route('/deletar/<int:id_game>')
def delete_game(id_game):
    game = Games.query.filter_by(id=id_game)
    url_game = game.first().url_image
    game.delete()
    try:
        delete_image(url_game)
    except FileNotFoundError as err:
        print(err, 'Jogo sem imagem cadastrada')

    except TypeError as err:
        print(err, 'Jogo sem imagem')

    else:
        print('Exclusão da imagem do jogo realizada com sucesso')

    db.session.commit()
    flash('Jogo deletado com sucesso', 'success')

    return redirect(url_for('index'))

