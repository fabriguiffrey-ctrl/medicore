from pydantic import BaseModel
<<<<<<< HEAD

# schema para login
class LoginRequest(BaseModel):
    email: str
    password: str
=======
from uuid import UUID

class UserOut(BaseModel):
    id: UUID
    clinic_id: UUID
    role: str
>>>>>>> 84b76c2771508275288ddeba9bf9e93e98db1d3d
