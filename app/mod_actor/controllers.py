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