import functools
from requests.exceptions import ConnectionError
from flask import request
from app.utils.external_services import verify_token


def validate_token(f):
    @functools.wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            token = request.headers.get("Authorization")
            if token is not None:
                is_token_valid = verify_token(token)
                if is_token_valid:
                    return f(*args, **kwargs)
                else:
                    return {"error": "Invalid Token"},401
            else:
                return {"error": "Authentication credentials not provided"}, 401
        except ConnectionError:
            return {"error": "Credentials could not be verified"}, 503
    return decorated_function
