from main import app, db
from models.users import *
from flask import render_template, session, redirect, url_for, flash, request
from forms.userForm import UserForm


"""view para atualizar dados do usuário"""
@app.route('/atualizar-cadastro', methods=['GET','POST'])
def user_update():
    if request.method == 'POST':
        user = Users.query.filter_by(nickname=session['user_logged']).first()
        new_name = request.form['name']
        new_nickname = request.form['user']
        password = request.form['password']

        if user.auth(password):
            user.name = new_name
            user.nickname = new_nickname

            db.session.add(user)
            db.session.commit()
            session['user_logged'] = user.nickname

            flash('Dados alterados com sucesso', 'success')
            return redirect(url_for('index'))

        else:
            flash('Senha inválida')
            return render_template('users/updateUser.html')

    else:
        if 'user_logged' in session and session['user_logged'] is not None:
            form = UserForm()
            nickname = session['user_logged']
            user = Users.query.filter_by(nickname=nickname).first()
            form.name.data = user.name
            form.nickname.data = user.nickname

            directory = 'default' if not user.url_image else 'user'
            file_name= user.url_image.split('/')[-1] if user.url_image else 'capa_padrao.jpg'

            context = {
                'directory': directory,
                'file_name': file_name,
            }

            return render_template('users/updateUser.html', data_user=user, form=form, context=context)
        else:
            flash('requisição inválida','danger')
            return redirect(url_for('index'))
