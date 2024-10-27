from flask import Flask
from os import getenv
from app.configs import database, migration, auth, cors
from app import routes
from dotenv import load_dotenv
from datetime import timedelta

load_dotenv()

def create_app():

    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = getenv("SQLALCHEMY_DATABASE_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JSON_SORT_KEYS"] = False
    app.config["SECRET_KEY"] = getenv("SECRET_KEY")
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)

    cors.init_app(app)
    database.init_app(app)
    migration.init_app(app)
    auth.init_app(app)
    routes.init_app(app)

    return app