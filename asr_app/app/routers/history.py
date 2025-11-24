from datetime import datetime
from typing import List, Optional

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from .. import schemas
from ..dependencies import get_current_driver, get_db
from ..models.eleos_history import EleosEventHistory, EleosHistoryStopsByLoad
from ..models.eleos_driver import EleosDriverCredentials

router = APIRouter(prefix="/history", tags=["history"])


@router.get("/events", response_model=List[schemas.history.EventHistory])
def list_events(
    limit: int = Query(50, ge=1, le=500),
    current_driver: EleosDriverCredentials = Depends(get_current_driver),
    db: Session = Depends(get_db),
):
    events = (
        db.query(EleosEventHistory)
        .filter(EleosEventHistory.DriverCode == str(current_driver.DriverID))
        .order_by(EleosEventHistory.EventDt.desc())
        .limit(limit)
        .all()
    )
    return [
        schemas.history.EventHistory(
            event_id=e.EventId,
            activity=e.Activity,
            event_dt=e.EventDt,
            latitude=e.Latitude,
            longitude=e.Longitude,
            odometer=e.Odometer,
            fuel_level=e.FuelLevel,
            order_number=e.OrderNumber,
            load_number=e.LoadNumber,
            shift_number=e.ShiftNumber,
            stop_number=e.StopNumber,
        )
        for e in events
    ]


@router.get("/stops", response_model=List[schemas.history.HistoryStop])
def list_history_stops(
    start: Optional[datetime] = Query(None),
    end: Optional[datetime] = Query(None),
    current_driver: EleosDriverCredentials = Depends(get_current_driver),
    db: Session = Depends(get_db),
):
    query = db.query(EleosHistoryStopsByLoad).filter(
        EleosHistoryStopsByLoad.DriverUptID == current_driver.DriverID
    )
    if start:
        query = query.filter(EleosHistoryStopsByLoad.EventDatetime >= start)
    if end:
        query = query.filter(EleosHistoryStopsByLoad.EventDatetime <= end)

    stops = query.order_by(EleosHistoryStopsByLoad.EventDatetime.desc()).all()
    return [
        schemas.history.HistoryStop(
            history_id=s.HistoryID,
            event_datetime=s.EventDatetime,
            activity=s.Activity,
            shift_detail=s.ShiftDetail,
            order_id=s.OrderID,
            load_num=s.LoadNum,
            load_num_ord=s.LoadNumOrd,
            driver_upt_id=s.DriverUptID,
            driver_name=s.DriverName,
            truck_upt_id=s.TruckUptID,
            trailer_upt_id=s.TrailerUptID,
            stop_type=s.StopType,
            stop_upt_id=s.StopUptID,
            stop_geotab_id=s.StopGeotabID,
            stop_name=s.StopName,
            stop_latitude=s.StopLatitude,
            stop_longitude=s.StopLongitude,
            stop_odometer=s.StopOdometer,
            stop_fuel_level=s.StopFuelLevel,
        )
        for s in stops
    ]

