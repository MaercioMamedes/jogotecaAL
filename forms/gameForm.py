from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,validators


class GameForm(FlaskForm):
    name = StringField('Nome do Jogo', [validators.DataRequired(), validators.length(max=50)])
    console = StringField('Console', [validators.DataRequired(), validators.length(max=50)])
    category = StringField('Categoria', [validators.DataRequired(), validators.length(max=20)])
    save = SubmitField('Salvar')
