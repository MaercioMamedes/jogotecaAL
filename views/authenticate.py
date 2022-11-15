from main import app
from flask import request, session, flash, redirect, url_for, render_template
from models.users import Users


@app.route('/authenticate', methods=['POST',])
def authenticate():
    user = Users.query.filter_by(nickname=request.form['user']).first()
    if user:
        if user.auth(request.form['password']):
            session['user_logged'] = user.nickname
            flash(user.nickname + ' logado com sucesso!', 'success')
            next_page = request.form['next-page']
            return redirect(next_page)
    else:
        flash('Usuário ou senha incorretos', 'danger')
        return redirect(url_for('login'))
