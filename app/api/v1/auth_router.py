from urllib.request import Request

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.auth import LoginRequest
from app.services.auth_service import login as login_service
from app.db.session import get_db
from app.core.security import get_current_user
from app.models.user import User


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.post("/login",)
def login(request: LoginRequest, db: Session = Depends(get_db)):
    return login_service(db, request)

@router.get("/me")
def get_me(current_user: User = Depends(get_current_user)):
    return {
        "id": current_user.id,
        "email": current_user.email,
        "created_at": current_user.created_at,
    }