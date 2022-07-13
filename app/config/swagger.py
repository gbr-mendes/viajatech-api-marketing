"""This module encopassing the config for swagger"""
from flask_swagger_ui import get_swaggerui_blueprint

SWAGGER_URL = "/swagger"
API_URL = "/static/swagger.json"
SWAGGER_CONFIG = {
    "app_name": "Viaja Tech Marketing API"
}

swagger_blueprint = get_swaggerui_blueprint(
    base_url=SWAGGER_URL,
    api_url=API_URL,
    config=SWAGGER_CONFIG
)
