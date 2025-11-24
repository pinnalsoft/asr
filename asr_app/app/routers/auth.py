from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from ..dependencies import get_current_driver, get_db
from ..models.eleos_driver import EleosDriverCredentials
from ..schemas.auth import DriverProfile, LoginRequest, Token
from ..utils.jwt import create_access_token

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/login", response_model=Token)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    driver: EleosDriverCredentials | None = (
        db.query(EleosDriverCredentials)
        .filter(EleosDriverCredentials.Username == form_data.username)
        .first()
    )
    if driver is None or driver.Password != form_data.password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )

    token = create_access_token({"driver_id": driver.DriverID, "username": driver.Username})
    return Token(access_token=token)


@router.get("/me", response_model=DriverProfile)
def read_current_driver(driver=Depends(get_current_driver)):
    return DriverProfile(
        driver_id=driver.DriverID,
        name=driver.Name,
        username=driver.Username,
        geotab_username=driver.GeotabUsername,
        geotab_password_status=driver.GeotabPasswordStatus,
    )
