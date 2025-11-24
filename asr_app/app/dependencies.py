from typing import Generator

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from .database import SessionLocal
from .models.eleos_driver import EleosDriverCredentials
from .utils.jwt import decode_access_token


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_current_driver(
    token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)
) -> EleosDriverCredentials:
    payload = decode_access_token(token)
    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    driver_id = payload.get("driver_id")
    username = payload.get("username")
    if driver_id is None or username is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token missing claims",
            headers={"WWW-Authenticate": "Bearer"},
        )

    driver = (
        db.query(EleosDriverCredentials)
        .filter(
            EleosDriverCredentials.DriverID == driver_id,
            EleosDriverCredentials.Username == username,
        )
        .first()
    )
    if driver is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Driver not found",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return driver
