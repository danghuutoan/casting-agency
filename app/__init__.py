


import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    CORS(app)

    return app


app = create_app()

# Configurations
app.config.from_object('config')
# by modules and controllers
db = SQLAlchemy(app)

from app.mod_actor.controllers import mod_actor as actor_module
from app.mod_movie.controllers import mod_movie as movie_module

app.register_blueprint(actor_module)
app.register_blueprint(movie_module)


@app.route('/')
def index():
    return "helloworld1"
