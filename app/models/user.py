from sqlalchemy import Column, Integer, String
<<<<<<< HEAD
from app.db.base import Base

class User(Base):

=======
from app.db.database import Base

class User(Base):
>>>>>>> 84b76c2771508275288ddeba9bf9e93e98db1d3d
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
<<<<<<< HEAD
    hashed_password = Column(String)
=======
    hashed_password = Column(String)
>>>>>>> 84b76c2771508275288ddeba9bf9e93e98db1d3d
