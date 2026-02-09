from fastapi import APIRouter, Depends, Request
from app.schemas.user import UserOut

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/me", response_model=UserOut)
def get_me(request: Request):
    if not request.state.user:
        return {"error": "Unauthorized"}

    return request.state.user
