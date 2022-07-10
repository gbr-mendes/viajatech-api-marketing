import os
from flask import request, redirect
import bson.json_util as json_util
from ..config.db import DB
from ..services.send_mail import send_single_email
from app.schemas.marketing import EmailMarketingSchema
from app.models.marketing import EmailMarketing
from app.utils.external_services import verify_token


def create_marketing_capaing():
    """Function responsible to deal with the request of marketing campaing creation and send of email marketing"""
    if request.json:
        token = request.headers.get("auth-token", None)
        token_is_valid =  verify_token(token)
        if token_is_valid:
            data = request.json
            email_marketing_collection = DB["EmailMarketing"]
            try:
                email = email_marketing_collection.insert_one({**data})
                if email is not None:
                    target_emails = data.pop("target_emails", None)
                    for email in target_emails:
                        data["target_email"] = email
                        send_single_email(**data)
                    return {"success": "Campaign created and emails sent"}, 201
            except Exception:
                return {"error": "An unexpected error occurred"}, 500
        else:
            return {"error": "Authentication required"}, 401
    return {"error": "You need to provide a valid payload"}


def list_emails_marketing():
    """This function goes to the database and get the list of the email marketing"""
    token = request.headers.get("auth-token", None)
    token_is_valid =  verify_token(token)
    if token_is_valid:
        email_marketing_collection = DB["EmailMarketing"]
        schema = EmailMarketingSchema()
        try:
            emails = email_marketing_collection.find()
            list_emails = [schema.dump(EmailMarketing(**email)) for email in emails]
            return {"emails": list_emails}
        except Exception as e:
            print(e)
            return {"error": "An unexpected error occurred"}, 500
    else:
        return {"error": "Authentication required"}


def disable_notifications():
    """This function is responsible for disable the notifications by email for a lead"""
    users_collection = DB["users"]
    email = request.args.get("lead_email")
    
    try:
        user= users_collection.find_one({"email": email})
        if user:
            users_collection.find_one_and_update({"email": email}, {"$set":{"notifications":False}})
            return redirect(os.getenv("REDIRECT_URI"))   
        else:
            return{"error": "user not found"}, 400
    except Exception:
        return {"error": "Failed to disabled notifications"}, 500
