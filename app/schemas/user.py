from pydantic import BaseModel

# schema para login
class LoginRequest(BaseModel):
    email: str
    password: str