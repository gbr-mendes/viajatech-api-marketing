"""This module is the gateway to the application"""
from flask import Flask
from .routes.send_mail import bp as send_mail_bp
from dotenv import load_dotenv

load_dotenv()


def create_app():
    """Function responsible to create an app instance"""
    app = Flask(__name__)
    app.register_blueprint(send_mail_bp, url_prefix="/api/v1")
    return app
