from flask import Blueprint
from app.routes.user_blueprint import bp_user

bp_api = Blueprint("bp_api", __name__, url_prefix="/api")

bp_api.get("/")
bp_api.register_blueprint(bp_user)