from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.user import User
from app.core.deps import get_current_user
from app.schemas.user import UserOut

router = APIRouter()

@router.get("/", response_model=list[UserOut], summary="List users")
def list_users(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user),
):
    return db.query(User).all()


@router.get("/me")
def get_me(current_user: User = Depends(get_current_user)):
    return current_user
