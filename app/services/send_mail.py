"""This module is responsible to encopassing all the services for sending email"""
import os
import requests

def send_single_email(target_email, subject, body, target_name=None):
    """This function sends  single email to the target"""
    return requests.post(
        os.getenv('MAILGUN_ENDPOINT'),
        auth=("api", os.getenv('MAILGUN_API_KEY')),
        data={"from": f"Viaja Tech <{os.getenv('MAILGUN_EMAIL_ORIGIN')}>",
            "to": f"{target_name} <{target_email}>",
            "subject":subject,
            "text": body
    })
