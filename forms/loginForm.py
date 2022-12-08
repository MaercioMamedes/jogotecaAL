from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, validators


class LoginForm(FlaskForm):
    nickname = StringField('Nickname', [validators.DataRequired(), validators.length(min=1, max=20)])
    password = PasswordField("Digite sua senha", [validators.DataRequired(), validators.length(min=4, max=100)])
    login = SubmitField("Login")
