from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from passlib.context import CryptContext

from .. import schemas
from ..dependencies import get_db, get_current_driver
from ..models.eleos_driver import EleosDriverCredentials
from ..utils.jwt import create_access_token

router = APIRouter(prefix="/auth", tags=["auth"])

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    if not hashed_password:
        return False
    if hashed_password.startswith("$2b$") or hashed_password.startswith("$2a$"):
        try:
            return pwd_context.verify(plain_password, hashed_password)
        except ValueError:
            return False
    return plain_password == hashed_password


@router.post("/login", response_model=schemas.auth.Token)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    user: EleosDriverCredentials | None = (
        db.query(EleosDriverCredentials)
        .filter(EleosDriverCredentials.Username == form_data.username)
        .first()
    )
    if not user or not verify_password(form_data.password, user.Password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    token, expires_at = create_access_token(
        {"driver_id": user.DriverID, "username": user.Username}
    )

    return schemas.auth.Token(
        access_token=token,
        expires_at=expires_at,
    )


@router.get("/me", response_model=schemas.auth.Driver)
def read_users_me(current_driver: EleosDriverCredentials = Depends(get_current_driver)):
    return schemas.auth.Driver(
        driver_id=current_driver.DriverID,
        name=current_driver.Name,
        username=current_driver.Username,
        geotab_username=current_driver.GeotabUsername,
        geotab_password_status=current_driver.GeotabPasswordStatus,
    )

