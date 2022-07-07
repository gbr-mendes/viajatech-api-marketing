import os
from flask import request, redirect
from models.db import DB

def disable_notifications():
    users_collection = DB.users
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
