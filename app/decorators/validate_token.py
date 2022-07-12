import functools
from flask import request
from app.utils.external_services import verify_token


def validate_token(f):
    @functools.wraps(f)
    def decorated_function(*args, **kwargs):
        token = request.headers.get("Authorization")
        if token is not None:
            token = token.split(" ")[1]
            is_token_valid = verify_token(token)
            if is_token_valid:
                return f(*args, **kwargs)
            else:
                return {"error": "Invalid Token"},401
        else:
            return {"error": "Authentication credentials not provided"}, 401
    return decorated_function
