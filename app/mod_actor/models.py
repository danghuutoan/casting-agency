from app import db
from app.mod_movie.models import movie_actor_table 

class Gender(db.Model):
    __tablename__ = 'gender'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    actors = db.relationship('Actor', back_populates='gender', lazy=True)

class Actor(db.Model):

    __tablename__ = 'actor'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    age = db.Column(db.Integer)
    gender_id = db.Column(db.Integer, db.ForeignKey('gender.id'))
    gender = db.relationship("Gender", back_populates="actors")

    movies = db.relationship("Movie",
                    secondary= movie_actor_table, back_populates="actors")
    
    def update(self):
        db.session.commit()

    def format(self):
        movies = []
        for movie in self.movies:
            movies.append(movie.format_short())
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "gender": self.gender_id,
            "movies": movies
        }
    
    def format_short(self):
        return {
            "id": self.id,
            "name": self.name
        }