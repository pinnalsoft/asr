from sqlalchemy import Column, DateTime, DECIMAL, Integer, String, PrimaryKeyConstraint

from ..database import Base


class EleosEventHistory(Base):
    __tablename__ = "EleosEventHistory"

    EventId = Column(Integer, primary_key=True, index=True)
    DriverCode = Column(String(50))
    TractorCode = Column(String(50))
    ZoneCode = Column(String(50))
    Activity = Column(String(100))
    TelematicsEventId = Column(String(100))
    EventDt = Column(DateTime)
    MessageHandle = Column(String(100))
    Latitude = Column(DECIMAL(9, 6))
    Longitude = Column(DECIMAL(9, 6))
    Odometer = Column(DECIMAL(10, 2))
    FuelLevel = Column(DECIMAL(5, 2))
    Trailer = Column(String(50))
    OrderNumber = Column(String(50))
    LoadNumber = Column(String(50))
    MoveNumber = Column(String(50))
    ShiftNumber = Column(String(50))
    StopNumber = Column(String(50))
    Started = Column(DateTime)
    Arrived = Column(DateTime)
    Departed = Column(DateTime)
    Ended = Column(DateTime)
    Processed = Column(DateTime)
    ReceivedDt = Column(DateTime)
    TransmitDelay = Column(Integer)


class EleosHistoryStopsByLoad(Base):
    __tablename__ = "EleosHistoryStopsByLoad"

    HistoryID = Column(Integer, primary_key=True, index=True)
    EleosEventID = Column(Integer)
    EventDatetime = Column(DateTime)
    Activity = Column(String(100))
    ShiftDetail = Column(Integer)
    OrderID = Column(Integer)
    LoadNum = Column(String(50))
    LoadNumOrd = Column(Integer)
    DriverUptID = Column(Integer)
    DriverName = Column(String(200))
    GeotabUsername = Column(String(100))
    TruckUptID = Column(Integer)
    TrailerUptID = Column(Integer)
    StopType = Column(String(50))
    StopUptID = Column(Integer)
    StopGeotabID = Column(String(100))
    StopName = Column(String(200))
    StopLatitude = Column(DECIMAL(9, 6))
    StopLongitude = Column(DECIMAL(9, 6))
    StopOdometer = Column(DECIMAL(10, 2))
    StopFuelLevel = Column(DECIMAL(5, 2))

