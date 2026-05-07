from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

from app.db.session import get_db
from app.services.user_service import authenticate_user
from app.core.security import create_access_token
from app.models.user import User
from app.core.security import get_password_hash
router = APIRouter()

@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    user = authenticate_user(db, form_data.username, form_data.password)

    if not user:
        raise HTTPException(status_code=401, detail="Credenciales inválidas")

    access_token = create_access_token({
    "sub": str(user.id),  
    "clinic_id": str(user.clinic_id),
    "role": user.role
})


    return {
        "access_token": access_token,
        "token_type": "bearer"
    }
    
@router.post("/register")
def register(
    email: str,
    password: str,
    db: Session = Depends(get_db)
):
     #Verifica si el usuario ya existe
    user = db.query(User).filter(User.email == email).first()
    if user:
        raise HTTPException(status_code=400, detail="El usuario ya existe")

    # Crear usuario
    new_user = User(
        email=email,
        hashed_password=get_password_hash(password),
        clinic_id=None,  # por ahora simple
        role="user"
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"msg": "Usuario creado correctamente"}

