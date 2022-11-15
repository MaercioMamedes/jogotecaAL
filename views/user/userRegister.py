from main import app, db
from flask import request, redirect, url_for, render_template, flash
from models.users import *


@app.route('/cadastro', methods=['GET','POST'])
def user_register():
    if request.method == 'POST':
        name = request.form['name']
        nickname = request.form['user']
        password = request.form['password']
        password_corfim = request.form['password-confirm']

        if not check_equal_password_input(password, password_corfim):
            flash('Senha inválida', 'danger')
            return render_template('userRegister.html')

        else:
            user = Users.create(nickname,name,password)
            db.session.add(user)
            db.session.commit()

            return redirect(url_for('index'))

    return render_template('userRegister.html')


def check_equal_password_input(password, password_confirm):
    return password_confirm == password