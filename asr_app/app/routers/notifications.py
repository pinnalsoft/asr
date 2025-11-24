from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..dependencies import get_current_driver, get_db
from ..models.eleos_driver import EleosDriverNotifications
from ..schemas.notification import NotificationAck, NotificationItem

router = APIRouter(prefix="/notifications", tags=["notifications"])


@router.get("/", response_model=list[NotificationItem])
def list_notifications(db: Session = Depends(get_db), driver=Depends(get_current_driver)):
    notifications = (
        db.query(EleosDriverNotifications)
        .filter(EleosDriverNotifications.DriverID == driver.DriverID)
        .all()
    )
    return [NotificationItem.from_orm(n) for n in notifications]


@router.post("/ack", response_model=NotificationAck)
def acknowledge_notification():
    # Placeholder acknowledging endpoint; real implementation would update database
    return NotificationAck()
