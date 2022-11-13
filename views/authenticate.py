from main import app
from flask import request, session, flash, redirect, url_for
from models.users import Users


@app.route('/authenticate', methods=['POST',])
def authenticate():
    user = Users.query.filter_by(nickname=request.form['usuario']).first()
    if user:
        if request.form['password'] == user.senha:
            session['user_logged'] = user.nickname
            flash(user.nickname + ' logado com sucesso!')
            proxima_pagina = request.form['proxima']
            return redirect(proxima_pagina)
    else:
        flash('Usuário não logado.')
        return redirect(url_for('login'))
