from main import app, db
from flask import flash, redirect, url_for
from models import Games


@app.route('/deletar/<int:id_game>')
def delete_game(id_game):
    Games.query.filter_by(id=id_game).delete()
    db.session.commit()
    flash('Jogo deletado com sucesso', 'success')
    return redirect(url_for('index'))

