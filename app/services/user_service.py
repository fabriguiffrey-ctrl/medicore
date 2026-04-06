from sqlalchemy.orm import Session
from app.models.user import User
from app.utils.security import hash_password, verify_password

# registramos user
def register_user(db: Session, email: str, password: str):
    hashed = hash_password(password)

    user = User(
        email=email,
        hashed_password=hashed
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


# función lOGIN
def authenticate_user(db: Session, email: str, password: str):
    user = db.query(User).filter(User.email == email).first()

    if not user:
        return None

    if not verify_password(password, user.hashed_password):
        return None

    return user


#print("PASSWORD RECIBIDO:", password, type(password)) HABILITAR EN ENTORNOS DE PRUEBA