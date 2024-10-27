from re import fullmatch, compile
from app.excepetions import EmailAlreadyExistsError, PatternEmailError
from app.excepetions.user_exception import InvalidKeyUserError, InvalidTypeUserError

# User Functions
def validate_user_data(data: dict):
    required_keys = {"name", "last_name", "email", "password"}
    
    if not required_keys.issubset(data.keys()) or len(data) != len(required_keys):
        raise InvalidKeyUserError(**data)
    
    if any(type(data[key]) != str for key in required_keys):
        raise InvalidTypeUserError(**data)


# Util Functions
def validate_email(data: dict, model):
    pattern_email = compile(r"([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\"([]!#-[^-~ \t]|(\\[\t -~]))+\")@([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\[[\t -Z^-~]*])")

    if "email" in data:
        email = data.get("email")
        if not fullmatch(pattern_email, email):
            raise PatternEmailError(email)
        
        if model.query.filter_by(email=email).first():
            raise EmailAlreadyExistsError(email)