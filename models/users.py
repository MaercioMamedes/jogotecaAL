from main import db


class Users(db.Model):
    nickname = db.Column(db.String(8), primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    password_hash = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name

    def __str__(self):
        return f'Usuário {self.name}'

    def auth(self):
        """Método para autenticar senha do usuário"""
        pass
