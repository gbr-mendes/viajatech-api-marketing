"""This module is responsible for encompassing the controller for sending email"""
from flask import request
from ..services.send_mail import send_single_email

def send_email():
    """Function responsible to deal with the request of send email"""
    if request.json:
        data = request.json

        target_email = data.get('target_email')
        target_name = data.get('target_name')
        subject = data.get('subject')
        body = data.get('body')

        send_single_email(target_email, target_name, subject, body)
        return {"success": "email sended successfuly"}
    
    return "it's working"
    