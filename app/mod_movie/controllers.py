# Import flask dependencies
from flask import Blueprint, request, render_template, \
    flash, g, session, redirect, url_for


# Import the database object from the main app module


# Import module forms


# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_movie = Blueprint('movies', __name__, url_prefix='/movies')

# Set the route and accepted methods


@mod_movie.route('/', methods=['GET'])
def actor_index():

    return "movies"
