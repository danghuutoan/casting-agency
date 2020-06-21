from app import db

movie_actor_table = db.Table('movie_actor', db.metadata,
    db.Column('movie_id', db.Integer, db.ForeignKey('movie.id')),
    db.Column('actor_id', db.Integer, db.ForeignKey('actor.id'))
    )

class Movie(db.Model):

    __tablename__ = 'movie'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    release_date =  db.Column(db.DateTime(timezone=True))
    actors = db.relationship("Actor",
                    secondary= movie_actor_table, back_populates="movies")

    def format(self):
        actors = []

        for actor in self.actors:
            actors.append(actor.format_short())
        
        return {
            "id": self.id,
            "title": self.title,
            "actors": actors
        }