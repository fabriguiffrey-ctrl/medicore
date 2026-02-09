from pydantic import BaseModel
from uuid import UUID

class UserOut(BaseModel):
    id: UUID
    clinic_id: UUID
    role: str
