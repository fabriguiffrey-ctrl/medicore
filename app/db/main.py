from fastapi import FastAPI

from app.db.database import Base, engine
from app.models import user 

app = FastAPI()

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)