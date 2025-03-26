from fastapi import APIRouter, Request
from app.schemas.user import Token
from app.services.auth_service import authenticate_user

router = APIRouter()

@router.post("/login", response_model=Token)
async def login(request: Request):
    data = await request.json()
    email = data.get("email")
    password = data.get("password")
    
    
    token = authenticate_user(email, password)
    if not token:
        return {"success": False,"error": "Invalid email or password", "access_token": None}
        
    return {"success": True,"access_token": token, "error": None}
