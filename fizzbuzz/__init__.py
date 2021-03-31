from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)

heroku_db_url = 'postgresql://psgsaifrjucpwf:da1deb4a94e5116f389bcae080c882f485482f3bf4a8b8146bc9e5a983c64a45@ec2-54-247-158-179.eu-west-1.compute.amazonaws.com:5432/dd3f9vjt6bvmvb'  # noqa
app.config['SQLALCHEMY_DATABASE_URI'] = heroku_db_url

# Creates an SQLAlchemy database instance
db = SQLAlchemy(app)

from fizzbuzz.models import Variables  # noqa

# flask-migrate setup
migrate = Migrate(app, db)

# Importing routes here to avoid circular imports,
# since routes imports the above 'app' variable
from fizzbuzz import routes  # noqa
