from main import db

users_games = db.Table('users_games',
                       db.Column('users_id', db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), primary_key=True,),
                       db.Column('games_id', db.Integer, db.ForeignKey('games.id', ondelete='CASCADE'), primary_key=True),
                       )
