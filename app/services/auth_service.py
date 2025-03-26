from app.services.user_service import get_user_by_email
from app.utils.security import verify_password, create_access_token

def authenticate_user(email: str, password: str):
    user = get_user_by_email(email)
    if not user or not verify_password(password, user['password']):
        return None
    return create_access_token({"sub": user['email']})