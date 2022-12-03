from flask import Flask
from flask_sqlalchemy import SQLAlchemy


"""Instaciação  da aplicação Flask"""
app = Flask(__name__)

"""Definições dos parâmetros de configuração da aplicação a partir do arquivo config.py"""
app.config.from_pyfile('config.py')

"""Instaciação do banco de dados da aplicação"""
db = SQLAlchemy(app)

from views.core.index import *
from views.core.login import *
from views.core.authenticate import *
from views.core.logout import *
from views.core.my_games import *
from views.core.remove_game import *
from views.core.index_users import *
from views.user.userRegister import *
from views.user.userUpdate import *
from views.game.newGame import *
from views.game.game import *
from views.game.deleteGame import *
from views.game.updateGame import *
from views.game.image import *

if __name__ == '__main__':
    app.run(debug=True)
