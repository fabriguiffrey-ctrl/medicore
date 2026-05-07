from fastapi import Depends, HTTPException
from jose import JWTError, jwt
from sqlalchemy.orm import Session
from uuid import UUID

from app.core.security import oauth2_scheme, SECRET_KEY, ALGORITHM, create_access_token
from app.db.database import SessionLocal
from app.models.user import User


# dependency base datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Obtener usuario desde token
def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("sub")

        if user_id is None:
            raise HTTPException(status_code=401, detail="Invalid token")

        user_id = UUID(user_id)

    except (JWTError, ValueError):
        raise HTTPException(status_code=401, detail="Invalid token")

    user = db.query(User).filter(User.id == user_id).first()

    if user is None:
        raise HTTPException(status_code=401, detail="User not found")

    return user