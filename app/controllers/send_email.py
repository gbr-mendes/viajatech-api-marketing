"""This module is responsible for encompassing the controller for sending email"""
from flask import request


def send_email():
    """Function responsible to deal with the request of send email"""
    if request.json:
        data = request.json
        target = data.get('target')
        subject = data.get('subject')
        email_content = data.get('body')
        return {"target": target, "subject":subject, "email_content": email_content}
    
    return "it's working"
    