# Import flask dependencies
from flask import Blueprint, request, render_template, \
    flash, g, session, redirect, url_for, jsonify, abort

from app.mod_actor.models import Actor
from app.mod_movie.models import Movie
# Import module forms


# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_actor = Blueprint('actors', __name__, url_prefix='/actors')

# Set the route and accepted methods


@mod_actor.route('/', methods=['GET'])
def get_actors():
    try:
        actors = Actor.query.all()
    except Exception:
        abort(422)
    
    data = []

    for actor in actors:
        data.append(actor.format())
    return jsonify({
        "success": True,
        "actors": data
    })


@mod_actor.route('/<int:id>', methods=['GET'])
def get_actor_by_id(id):
    try:
        actor = Actor.query.get(id)
    except Exception:
        abort(422)
    if actor == None:
        abort(404)
    
    return jsonify({
        "success": True,
        "actors": actor.format()
    })


@mod_actor.route('', methods=['POST'])
def create_actor():
    request_json = request.get_json()
    actor = Actor(request_json["name"], request_json["age"], request_json["gender"])
    if "movies" in request_json:
        for movie_id in request_json['movies']:
            movie = Movie.query.get(movie_id)
            if movie == None:
                abort(400)
            actor.movies.append(movie) 
    
    actor.insert()
    return jsonify({
        "success": True,
        "actors": [actor.format()]
    })

@mod_actor.route('/<int:id>', methods=["DELETE"])
def delete_actor(id):
    actor = Actor.query.get(id)
    if actor == None:
        abort(404)
    else:
        actor.delete()

        return jsonify({
            "success": True,
            "delete": actor.id
        })

@mod_actor.route('/<int:id>', methods=["PATCH"])
def update_actor(id):
    actor = Actor.query.get(id)
    request_json = request.get_json()

    if actor == None:
        abort(404)
    else:
        for key in request_json:
            if key != "movies":
                if hasattr(actor, key) is False:
                    abort(400)
                setattr(actor, key, request_json[key])
            else:
            
                for movie_id in request_json["movies"]:
                    movie = Movie.query.get(movie_id)
                    if movie == None:
                        abort(400)
                    else:
                        actor.movies.append(movie)

        actor.update()

        return jsonify({
            "success": True,
            "update": actor.format()
        })