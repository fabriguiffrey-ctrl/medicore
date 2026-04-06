from passlib.context import CryptContext

# Configuración del algoritmo
pwd_context = CryptContext(
    schemes=["bcrypt"], #SALT + SECURIDAD = STANDARD SEGURO
    deprecated="auto"
)

#FUNCIONES:

# HASHEA EL PASS
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

# VERIFICA EL PASS EN EL LOGIN (Compara lo que ingresa el usuario contra lo guardado en BD)
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


from datetime import datetime, timedelta
from jose import jwt

SECRET_KEY = "tu_clave_secreta_super_segura"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt

