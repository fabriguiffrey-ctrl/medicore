from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from app.core.security import decode_token

class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):

        auth = request.headers.get("Authorization")
        request.state.user = None

        if auth and auth.startswith("Bearer "):
            token = auth.split(" ")[1]
            request.state.user = decode_token(token)

        return await call_next(request)
