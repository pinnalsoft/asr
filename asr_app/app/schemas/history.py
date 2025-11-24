from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel


class EventHistoryItem(BaseModel):
    EventId: int
    DriverCode: Optional[str]
    TractorCode: Optional[str]
    ZoneCode: Optional[str]
    Activity: Optional[str]
    TelematicsEventId: Optional[str]
    EventDt: Optional[datetime]
    MessageHandle: Optional[str]
    Latitude: Optional[float]
    Longitude: Optional[float]
    Odometer: Optional[float]
    FuelLevel: Optional[float]
    Trailer: Optional[str]
    OrderNumber: Optional[str]
    LoadNumber: Optional[str]
    MoveNumber: Optional[str]
    ShiftNumber: Optional[str]
    StopNumber: Optional[str]
    Started: Optional[datetime]
    Arrived: Optional[datetime]
    Departed: Optional[datetime]
    Ended: Optional[datetime]
    Processed: Optional[datetime]
    ReceivedDt: Optional[datetime]
    TransmitDelay: Optional[int]

    class Config:
        orm_mode = True


class HistoryStopItem(BaseModel):
    HistoryID: int
    EleosEventID: Optional[int]
    EventDatetime: Optional[datetime]
    Activity: Optional[str]
    ShiftDetail: Optional[int]
    OrderID: Optional[int]
    LoadNum: Optional[str]
    LoadNumOrd: Optional[int]
    DriverUptID: Optional[int]
    DriverName: Optional[str]
    GeotabUsername: Optional[str]
    TruckUptID: Optional[int]
    TrailerUptID: Optional[int]
    StopType: Optional[str]
    StopUptID: Optional[int]
    StopGeotabID: Optional[str]
    StopName: Optional[str]
    StopLatitude: Optional[float]
    StopLongitude: Optional[float]
    StopOdometer: Optional[float]
    StopFuelLevel: Optional[float]

    class Config:
        orm_mode = True


class HistoryStopFilter(BaseModel):
    start: Optional[datetime]
    end: Optional[datetime]
    limit: Optional[int] = 100


class EventQueryParams(BaseModel):
    limit: int = 50
