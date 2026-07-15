from sqlalchemy.orm import Session
from fastapi import HTTPException
from starlette import status

from app.models.user import User
from app.core.security import verify_password, create_access_token, create_refresh_token



def login(db: Session, email: str, password: str):
    user = db.query(User).filter(User.email == email).first()
    if not user:
        raise HTTPException(status_code=400, detail="Invalid email or password")

    if not verify_password(password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid email or password")

    token = create_access_token(data={"sub": str(user.id)})
    refresh_token = create_refresh_token(data={"sub": str(user.id)})
    return {
        "access_token": token,
        "refresh_token": refresh_token,
        "token_type": "bearer",
    }