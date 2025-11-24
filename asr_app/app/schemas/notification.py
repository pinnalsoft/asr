from typing import Optional

from pydantic import BaseModel


class NotificationItem(BaseModel):
    DriverID: int
    Username: str
    MessageBody: Optional[str]
    Contact: Optional[str]
    Sound: Optional[str]

    class Config:
        orm_mode = True


class NotificationAck(BaseModel):
    acknowledged: bool = True
