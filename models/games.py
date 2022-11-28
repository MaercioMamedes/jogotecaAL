from main import db


"""Modelo da classe Game, define os atributos e seus métodos"""


class Games(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    console = db.Column(db.String(50), nullable=False)
    category = db.Column(db.String(20), nullable=False)
    created_by = db.Column(db.String(50), nullable=False)
    created_on = db.Column(db.DateTime(timezone=False))
    updated_on = db.Column(db.DateTime(timezone=False))
    url_image = db.Column(db.String(150))

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'<Name {self.name}>'
