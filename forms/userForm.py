from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, validators


class UserForm(FlaskForm):
    name = StringField('Nome Completo', [validators.DataRequired(), validators.length(min=1, max=20)])
    nickname = StringField('Nickname', [validators.DataRequired(), validators.length(min=1, max=20)])
    password = PasswordField('Senha', [validators.DataRequired(), validators.length(min=4, max=100)])
    password_confirm = PasswordField('Confirme sua senha', [validators.DataRequired(), validators.length(min=4, max=100)])
    save = SubmitField('Salvar')