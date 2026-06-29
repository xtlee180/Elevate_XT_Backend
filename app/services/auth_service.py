from sqlalchemy.orm import Session
from fastapi import HTTPException
from starlette import status

from app.models.user import User
from app.schemas.auth import LoginRequest
from app.core.security import verify_password, create_access_token



def login(db: Session, request: LoginRequest):
    # 1. Find user by email
    user = db.query(User).filter(User.email == request.email).first()
    if not user:
        raise HTTPException(status_code=400, detail="Invalid email or password")

    # 2. Verify password
    if not verify_password(request.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid email or password")

    # 3. Generate JWT token
    token = create_access_token(data={"sub": str(user.id)})

    # 4. Return token
    return {
        "access_token": token,
        "token_type": "bearer"
    }