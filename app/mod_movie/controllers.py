# Import flask dependencies
from flask import Blueprint, request, render_template, \
    flash, g, session, redirect, url_for, jsonify, abort


# Import the database object from the main app module

from app.mod_movie.models import Movie

# Import module forms


# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_movie = Blueprint('movies', __name__, url_prefix='/movies')

# Set the route and accepted methods


@mod_movie.route('/', methods=['GET'])
def get_all_movies():
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
def get_movie_by_id(id):
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
