from typing import Optional

from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class TokenPayload(BaseModel):
    driver_id: int
    username: str


class LoginRequest(BaseModel):
    username: str
    password: str


class DriverProfile(BaseModel):
    driver_id: int
    name: Optional[str]
    username: str
    geotab_username: Optional[str]
    geotab_password_status: Optional[str]

    class Config:
        orm_mode = True
