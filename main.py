from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)

from views.index import *
from views.login import *
from views.authenticate import *

if __name__ == '__main__':
    app.run(debug=True)
