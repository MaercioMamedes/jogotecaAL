from main import db
import bcrypt


class Users(db.Model):
    @staticmethod
    def create(nickname_user, name_user, password):
        """Método que cria uma instância de User, e cria um hash para a senha do usuário"""
        # implementar método para garantir que um objeto instanciado seja sempre realizado pelo método create
        password = bytes(password, 'utf-8')
        password_hash_user = bcrypt.hashpw(password, bcrypt.gensalt())
        password_hash_user = str(password_hash_user, 'utf-8')
        user = Users(nickname=nickname_user, name=name_user, password_hash=password_hash_user)
        return user

    """Os atributos de um objeto Users, são otimizados, especialmente o password_hash. Quando o objeto é instaciando
    a partir do método stático Users.create"""

    nickname = db.Column(db.String(8), primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    password_hash = db.Column(db.String(100), nullable=False)

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
