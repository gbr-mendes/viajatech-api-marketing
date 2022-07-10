"""This module is responsible for encompassing the controller for sending email"""
from flask import request
from ..services.send_mail import send_single_email

def send_email():
    """Function responsible to deal with the request of send email"""
    if request.json:
        data = request.json
        send_single_email(**data)
        return {"success": "email sended successfuly"}
    
    return {"error": "You need to provide a valid payload"}    
