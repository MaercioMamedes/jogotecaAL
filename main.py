from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)

from views.core.index import *
from views.user.login import *
from views.user.authenticate import *
from views.user.logout import *
from views.user.userRegister import *
from views.user.userUpdate import *

"""from views.index import index
from views.login import login
from views.authenticate import authenticate"""

if __name__ == '__main__':
    app.run(debug=True)
