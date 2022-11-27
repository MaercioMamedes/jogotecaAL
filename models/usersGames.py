from main import db

users_games = db.Table('users_games',
                       db.Column('users_id', db.Integer, db.ForeignKey('user.id')),
                       db.Column('games_id', db.Integer, db.ForeignKey('game.id')),
                       )
