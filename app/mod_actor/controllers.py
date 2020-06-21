# Import flask dependencies
from flask import Blueprint, request, render_template, \
    flash, g, session, redirect, url_for

from .models import Actor
# Import module forms


# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_actor = Blueprint('actors', __name__, url_prefix='/actors')

# Set the route and accepted methods


@mod_actor.route('/', methods=['GET'])
def actor_index():

    return "actor"
