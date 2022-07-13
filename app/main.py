"""This module is the gateway to the application"""
import os

from flask import Flask
from dotenv import load_dotenv

from app.routes.send_mail import bp as send_mail_bp
from app.routes.marketing_management import bp as marketing_management_bp
from app.config.marshmallow import MA
from app.config.swagger import swagger_blueprint

load_dotenv()



def create_app(test_config=None):
    """Function responsible to create an app instance"""
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        app.config.from_mapping(
            SECRET_KEY=os.getenv("SECRET_KEY"),
        )
    else:
        app.config.from_mapping(test_config)

    app.register_blueprint(send_mail_bp, url_prefix="/api/v1")
    app.register_blueprint(marketing_management_bp, url_prefix="/api/v1/marketing")
    app.register_blueprint(swagger_blueprint, url_prefix="/swagger")

    MA.app = app

    return app
