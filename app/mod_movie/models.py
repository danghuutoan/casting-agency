from app import db
import datetime

movie_actor_table = db.Table('movie_actor', db.metadata,
    db.Column('movie_id', db.Integer, db.ForeignKey('movie.id')),
    db.Column('actor_id', db.Integer, db.ForeignKey('actor.id'))
    )

class Movie(db.Model):

    __tablename__ = 'movie'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    release_date =  db.Column(db.DateTime(timezone=True))
    actors = db.relationship("Actor",
                    secondary= movie_actor_table, back_populates="movies")

    def __init__(self, title, release_date):
        self.title = title
        self.release_date = datetime.datetime.strptime(release_date, "%Y-%m-%d %H:%M:%S")

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        actors = []

        for actor in self.actors:
            actors.append(actor.format_short())
        
        return {
            "id": self.id,
            "title": self.title,
            "release_date": self.release_date,
            "actors": actors
        }

    def format_short(self):
        
        return {
            "id": self.id,
            "title": self.title
        }