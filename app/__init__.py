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
# by modules and controllers
db = SQLAlchemy(app)


@app.route('/')
def index():
    return "helloworld1"
