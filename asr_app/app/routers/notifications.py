from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from .. import schemas
from ..dependencies import get_current_driver, get_db
from ..models.eleos_driver import EleosDriverCredentials, EleosDriverNotifications

router = APIRouter(prefix="/notifications", tags=["notifications"])


@router.get("", response_model=List[schemas.notification.DriverNotification])
def get_notifications(
    current_driver: EleosDriverCredentials = Depends(get_current_driver),
    db: Session = Depends(get_db),
):
    notifications = (
        db.query(EleosDriverNotifications)
        .filter(EleosDriverNotifications.DriverID == current_driver.DriverID)
        .all()
    )
    return [
        schemas.notification.DriverNotification(
            driver_id=n.DriverID,
            username=n.Username,
            message_body=n.MessageBody,
            contact=n.Contact,
            sound=n.Sound,
        )
        for n in notifications
    ]


@router.post("/ack", response_model=schemas.notification.NotificationAck)
def acknowledge_notifications(
    current_driver: EleosDriverCredentials = Depends(get_current_driver),
):
    return schemas.notification.NotificationAck(acknowledged=True)

