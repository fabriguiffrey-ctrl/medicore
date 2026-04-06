from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import SessionLocal
from app.services.user_service import register_user, authenticate_user
from app.schemas.user import LoginRequest  # importamos el eschema!!!
from fastapi.security import OAuth2PasswordRequestForm
from app.utils.security import create_access_token

router = APIRouter()

# dependencia para DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


from fastapi.security import OAuth2PasswordRequestForm

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)

    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token(data={"sub": user.email})

    return {
        "access_token": token,
        "token_type": "bearer"
    }