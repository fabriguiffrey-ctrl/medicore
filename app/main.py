from fastapi import FastAPI
from app.api.users import router as users_router
from app.middleware.auth import AuthMiddleware

app = FastAPI()

app.add_middleware(AuthMiddleware)

app.include_router(users_router)

@app.get("/health")
def health():
    return {"status": "ok"}

