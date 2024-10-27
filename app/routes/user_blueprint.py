from flask import Blueprint
from app.controllers.user_controller import registering_user

bp_user = Blueprint("bp_user", __name__, url_prefix="/users")

bp_user.post("/user/signup")(registering_user)