from main import app
from flask import request, session, flash, redirect, url_for, render_template
from models.users import Users


@app.route('/authenticate', methods=['POST',])
def authenticate():
    username = request.form['user']
    password = request.form['password']
    user = Users.query.filter_by(nickname=username).first()

    if user is not None and user.auth(password):
        session['user_logged'] = user.nickname
        flash(user.nickname + ' logado com sucesso!', 'success')
        next_page = request.form['next-page']

        return redirect(url_for(next_page))
    else:
        flash('Usuário ou senha incorretos', 'danger')
        return redirect(url_for('login'))
