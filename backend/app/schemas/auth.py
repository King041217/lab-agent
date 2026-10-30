from pydantic import BaseModel

from app.schemas.user import UserResponse


class Token(BaseModel):
    access_token: str
    token_type: str

class LoginRequest(BaseModel):
    username: str
    password: str


class LoginResponse(BaseModel):
    token: str
    user: UserResponse


class RegisterRequest(BaseModel):
    username: str
    password: str
    name: str | None = None
