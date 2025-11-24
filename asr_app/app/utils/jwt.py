from datetime import datetime, timedelta, timezone
from typing import Optional

from jose import JWTError, jwt

from ..config import get_settings

settings = get_settings()


def create_access_token(data: dict) -> tuple[str, datetime]:
    expire = datetime.now(timezone.utc) + timedelta(hours=settings.jwt_expires_in_hours)
    to_encode = data.copy()
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.jwt_secret, algorithm="HS256")
    return encoded_jwt, expire


def decode_access_token(token: str) -> Optional[dict]:
    try:
        payload = jwt.decode(token, settings.jwt_secret, algorithms=["HS256"])
        return payload
    except JWTError:
        return None

