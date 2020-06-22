# Import flask dependencies
from flask import Blueprint, request, render_template, \
    flash, g, session, redirect, url_for, jsonify, abort


# Import the database object from the main app module

from app.mod_movie.models import Movie
from app.mod_actor.models import Actor
# Import module forms
from app.auth.auth import requires_auth

# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_movie = Blueprint('movies', __name__, url_prefix='/movies')

# Set the route and accepted methods


@mod_movie.route('/', methods=['GET'])
@requires_auth('read:movies')
def get_all_movies(payload):
    try:
        movies = Movie.query.all()
    except Exception:
        abort(422)
    data = []

    for movie in movies:
        data.append(movie.format())
    return jsonify({
        "success": True,
        "movies": data
    })


@mod_movie.route('/<int:id>', methods=['GET'])
@requires_auth('read:movies')
def get_movie_by_id(payload,id):
    try:
        movie = Movie.query.get(id)
    except Exception:
        abort(422)
    
    if movie == None:
        abort(404)

    return jsonify({
        "success": True,
        "movies": movie.format()
    })

@mod_movie.route('', methods=['POST'])
@requires_auth('create:movies')
def create_movie(payload):
    request_json = request.get_json()
    movie = Movie(request_json["title"], request_json["release_date"])
    if "actors" in request_json:
        for actor_id in request_json['actors']:
            actor = Actor.query.get(actor_id)
            if actor == None:
                abort(400)
            movie.actors.append(actor) 
    
    movie.insert()
    return jsonify({
        "success": True,
        "movies": [movie.format()]
    })

@mod_movie.route('/<int:id>', methods=["DELETE"])
@requires_auth('delete:movies')
def delete_movie(payload, id):
    movie = Movie.query.get(id)
    if movie == None:
        abort(404)
    else:
        movie.delete()

        return jsonify({
            "success": True,
            "delete": movie.id
        })

@mod_movie.route('/<int:id>', methods=["PATCH"])
@requires_auth('update:movies')
def update_movie(payload, id):
    movie = Movie.query.get(id)
    request_json = request.get_json()

    if movie == None:
        abort(404)
    else:
        for key in request_json:
            if key != "actors":
                if hasattr(movie, key) is False:
                    abort(400)
                setattr(movie, key, request_json[key])
            else:
            
                for actor_id in request_json["actors"]:
                    actor = Actor.query.get(actor_id)
                    if actor == None:
                        abort(400)
                    else:
                        movie.actors.append(actor)

        movie.update()

        return jsonify({
            "success": True,
            "update": movie.format()
        })
