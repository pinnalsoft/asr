from datetime import datetime
from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
    expires_at: datetime


class TokenData(BaseModel):
    driver_id: int
    username: str


class LoginRequest(BaseModel):
    username: str
    password: str


class Driver(BaseModel):
    driver_id: int
    name: str | None = None
    username: str
    geotab_username: str | None = None
    geotab_password_status: str | None = None

    class Config:
        from_attributes = True

