from jose import jwt, JWTError
from uuid import UUID

SECRET_KEY = "super-secret-key"
ALGORITHM = "HS256"

def decode_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return {
            "id": UUID(payload["sub"]),
            "clinic_id": UUID(payload["clinic_id"]),
            "role": payload["role"],
        }
    except JWTError:
        return None
