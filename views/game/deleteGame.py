from main import app, db
from flask import flash, redirect, url_for
from models import Games
import os


@app.route('/deletar/<int:id_game>')
def delete_game(id_game):
    game = Games.query.filter_by(id=id_game)
    url_game = game.first().url_image
    game.delete()
    try:
        os.remove(url_game)
    except FileNotFoundError:
        print('Jogo sem imagem cadastrada')
    else:
        print('Exclusão da imagem do jogo realizada com sucesso')

    db.session.commit()
    flash('Jogo deletado com sucesso', 'success')

    return redirect(url_for('index'))

