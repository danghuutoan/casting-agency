from app import db
from app.mod_movie.models import movie_actor_table 

class Gender(db.Model):
    __tablename__ = 'gender'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    actors = db.relationship('actor', backref='gender', lazy=True)

class Actor(db.Model):

    __tablename__ = 'actor'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    age = db.Column(db.Integer)
    gender = db.Column(db.Integer, db.ForeignKey('gender.id'))
    movies = db.relationship("movie",
                    secondary= movie_actor_table)