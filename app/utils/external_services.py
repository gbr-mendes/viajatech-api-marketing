import requests, os

EXTERNAL_SERVICES_URL = os.getenv("EXTERNAL_SERVICES_URL")

def verify_token(token):
    """verify token authenticity"""
    response = requests.get(f"{EXTERNAL_SERVICES_URL}/users/verify-token", headers={"Authorization": token})
    success = response.json().get("sucesso")
    
    if success is not None:
        return True
    return False
