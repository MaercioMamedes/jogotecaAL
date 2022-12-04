from main import app, db
from flask import request, session, flash, redirect, url_for, render_template
from models.users import Users
from werkzeug.exceptions import NotFound



"""View responsável pela autenticação de usuário"""
@app.route('/authenticate', methods=['POST',])
def authenticate():
    username = request.form['user']
    password = request.form['password']

    try:
        user = Users.query.filter_by(nickname=username).first_or_404()
    except NotFound as err: # Testar
        print(err)
        user = None

    if user is not None and user.auth(password):
        session['user_logged'] = user.nickname
        session['is_adm'] = user.is_adm
        flash(user.nickname + ' logado com sucesso!', 'success')
        next_page = request.form['next-page']

        return redirect(url_for(next_page))
    else:
        flash('Usuário ou senha incorretos', 'danger')
        return redirect(url_for('login'))
