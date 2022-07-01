"""This module is responsible for encompassing the routes for the send mail methods"""
from flask import Blueprint
from ..controllers.send_email import send_email

bp = Blueprint('routes', __name__)

bp.route('/send-email', methods=["POST"])(send_email)
