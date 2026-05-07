from pydantic import BaseModel


# schema para login
class LoginRequest(BaseModel):
    email: str
    password: str

from uuid import UUID

class UserOut(BaseModel):
    id: UUID
    clinic_id: UUID
    role: str

