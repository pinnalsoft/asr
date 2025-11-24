from pydantic import BaseModel
from typing import Optional


class DriverNotification(BaseModel):
    driver_id: int
    username: str
    message_body: str
    contact: Optional[str]
    sound: Optional[str]

    class Config:
        from_attributes = True


class NotificationAck(BaseModel):
    acknowledged: bool = True

