<<<<<<< HEAD
from fastapi import FastAPI
from app.api.routes import users  

app = FastAPI()


app.include_router(users.router)

@app.get("/")
def root():
    return {"message": "API funcionando"}
=======
from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from app.db.database import engine, Base
import app.db.models  # Importa todos los modelos

from app.api.users import router as users_router
from app.middleware.auth import AuthMiddleware

app = FastAPI()

# Crea tablas si no existen
Base.metadata.create_all(bind=engine)

app.add_middleware(AuthMiddleware)
app.include_router(users_router)

@app.get("/health")
def health():
    return {"status": "ok"}

>>>>>>> 84b76c2771508275288ddeba9bf9e93e98db1d3d
