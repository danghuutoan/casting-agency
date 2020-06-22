


import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

def setup_db(app, database_path=os.environ.get("DATABASE_URL")):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()
    
def register_endpoint(app):
    from app.mod_actor.controllers import mod_actor as actor_module
    from app.mod_movie.controllers import mod_movie as movie_module

    app.register_blueprint(actor_module)
    app.register_blueprint(movie_module)

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    CORS(app)
    # Configurations
    app.config.from_object('config')
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "Not Found"
        }), 404
    
    @app.errorhandler(422)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "Unprocessable"
        }), 422
    
    @app.errorhandler(400)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "bad request"
        }), 400
    return app



app = create_app()
# by modules and controllers
db = SQLAlchemy(app)

setup_db(app)
register_endpoint(app)


@app.route('/')
def index():
    return "helloworld1"

