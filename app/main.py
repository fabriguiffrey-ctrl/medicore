from fastapi import FastAPI
from dotenv import load_dotenv

from app.db.database import engine, Base
import app.models.user

from app.api.routes import auth
from app.api.routes.users import router as users_router

from app.middleware.auth import AuthMiddleware

load_dotenv()

app = FastAPI()

# Crear tablas
Base.metadata.create_all(bind=engine)

# Middleware
app.add_middleware(AuthMiddleware)

# Rutas
app.include_router(users_router, prefix="/users", tags=["Users"])
app.include_router(auth.router, tags=["Auth"])

# Health check
@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/")
def root():
    return {"message": "API funca 🚀"}