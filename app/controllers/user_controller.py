from flask import request, current_app, jsonify
from app.models.user_model import UserModel
from app.controllers import validate_user_data, validate_email
from app.excepetions import EmailAlreadyExistsError, PatternEmailError
from app.excepetions.user_exception import InvalidKeyUserError, InvalidTypeUserError

def registering_user():
    data: dict = request.get_json()

    try:
        validate_user_data(data)
        validate_email(data, UserModel)
        
        password_to_hash = data.pop("password")

        user = UserModel(**data)
        
        user.password = password_to_hash

        current_app.db.session.add(user)
        
        current_app.db.session.commit()
        
    except (
        InvalidKeyUserError, 
        InvalidTypeUserError,
        PatternEmailError
        ) as error:
        return jsonify(error.message), 400

    except EmailAlreadyExistsError as error:
        return jsonify(error.message), 409

    return jsonify(user), 201