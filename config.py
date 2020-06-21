import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database


# TODO IMPLEMENT DATABASE URL
# SQLALCHEMY_DATABASE_URI = 'postgres://postgres@localhost:5432/casting_agency'
SQLALCHEMY_DATABASE_URI = 'postgres://xnosmblujpcipz:36607d3553168132f34ae90933b8629522a941f305e1094b6bdb6e787aa67122@ec2-52-72-221-20.compute-1.amazonaws.com:5432/ddj54gsu1fq5dm'
SQLALCHEMY_TRACK_MODIFICATIONS = False
