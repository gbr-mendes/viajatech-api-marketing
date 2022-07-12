"""This module is responsible to encopassing all the services for sending email"""
import os
from json import dumps
import requests

def send_single_email(target_email, subject, body, target_name=None, btn_link=None, track_marketing_url=None):
    """This function sends  single email to the target"""
    data = {"from": f"Viaja Tech <{os.getenv('MAILGUN_EMAIL_ORIGIN')}>",
            "to": f"{target_name} <{target_email}>",
            "subject":subject,
            "o:tracking": False,
            "template": "unsubscribe"
    }

    if btn_link and track_marketing_url:
        data["h:X-Mailgun-Variables"] = dumps({"btn_link": btn_link, "track_marketing_url": track_marketing_url, "message": body})
    else:
        data["h:X-Mailgun-Variables"] = dumps({"message": body})

    return requests.post(
        os.getenv('MAILGUN_ENDPOINT'),
        auth=("api", os.getenv('MAILGUN_API_KEY')),
        data=data)
