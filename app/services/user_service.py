import json
from pathlib import Path
from constants import JSON_PATH

def get_user_by_email(email: str):

    with open(JSON_PATH, "r") as f:
        users = json.load(f)

    for user in users:
        if user["email"] == email:
            return {
                "email": user["email"],
                "password": user["password"],
                "username": user["username"],
                "role": user["role"]
            }
    
    return None
