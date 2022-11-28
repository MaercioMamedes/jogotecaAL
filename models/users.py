from main import db
import bcrypt
from .usersGames import *
from models.games import *
from datetime import datetime


class Users(db.Model):
    @staticmethod
    def create(nickname_user, name_user, password):
        """Método que cria uma instância de User, e cria um hash para a senha do usuário"""
        # implementar método para garantir que um objeto instanciado seja sempre realizado pelo método create
        password = bytes(password, 'utf-8')
        password_hash_user = bcrypt.hashpw(password, bcrypt.gensalt())
        password_hash_user = str(password_hash_user, 'utf-8')
        created = datetime.now()
        user = Users(nickname=nickname_user,
                     name=name_user,
                     password_hash=password_hash_user,
                     created_on=created,
                     quantity_games=0)
        return user

    """Os atributos de um objeto Users, são otimizados, especialmente o password_hash. Quando o objeto é instaciando
    a partir do método stático Users.create"""

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nickname = db.Column(db.String(20), primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    created_on = db.Column(db.DateTime(timezone=False))
    is_adm = db.Column(db.Boolean())
    password_hash = db.Column(db.String(100), nullable=False)
    quantity_games = db.Column(db.Integer)
    games = db.relationship('Games', secondary=users_games, lazy='subquery',
                            backref=db.backref('users', lazy=True),
                            )

    def __repr__(self):
        return '<Name %r>' % self.name

    def __str__(self):
        return f'Usuário {self.name} ' \
               f'nickname: {self.nickname}'

    def auth(self, password):
        """Método para autenticar senha do usuário"""
        password = bytes(password,'utf-8')
        # retorna True se a senha for verdadeira, caso contrário retorna False
        if bcrypt.checkpw(password, bytes(self.password_hash, 'utf-8')):
            return True
        else:
            return False

    def add_game(self, game):
        self.games.append(game)
        self.quantity_games = len(self.games)

    def remove_game(self, game):
        self.games.remove(game)
        self.quantity_games = len(self.games)

