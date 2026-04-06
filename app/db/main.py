from fastapi import FastAPI
from app.db.database import engine
from app.db.base import Base

app = FastAPI()

Base.metadata.create_all(bind=engine)

from app.api.routes import users

app.include_router(users.router)