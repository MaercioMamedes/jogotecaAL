from main import app, db
from flask import request, redirect, url_for, render_template, flash
from models.users import *
from forms.userForm import UserForm
import time


"""View para cadastrar novo usuário"""
@app.route('/cadastro', methods=['GET','POST'])
def user_register():

    # Fazer validação de formulários em outra dependência

    if request.method == 'POST':
        form = UserForm(request.form)
        name = form.name.data
        nickname = form.nickname.data
        password = form.password.data
        password_corfim = form.password_confirm.data

        if not check_equal_password_input(password, password_corfim):
            flash('Senha inválida', 'danger')
            return render_template('users/userRegister.html')

        else:
            user = Users.create(nickname,name,password)
            db.session.add(user)
            db.session.commit()

            # Upload of the image to Application
            image_user = request.files['image']

            if image_user:
                upload_path = app.config['UPLOAD_PATH']
                url_image = f'{upload_path}/user/avatar-{user.id}-{time.time()}.jpg'
                image_user.save(url_image)

                # save url image in to Data Base
                user.url_image = url_image
                db.session.add(user)
                db.session.commit()

            return redirect(url_for('index'))

    form = UserForm()
    return render_template('users/userRegister.html', form=form)


def check_equal_password_input(password, password_confirm):
    return password_confirm == password
