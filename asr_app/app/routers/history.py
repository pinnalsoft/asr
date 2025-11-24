from datetime import datetime
from typing import List, Optional

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from ..dependencies import get_current_driver, get_db
from ..models.eleos_history import EleosEventHistory, EleosHistoryStopsByLoad
from ..schemas.history import EventHistoryItem, HistoryStopItem

router = APIRouter(prefix="/history", tags=["history"])


@router.get("/events", response_model=List[EventHistoryItem])
def list_events(
    limit: int = Query(50, ge=1, le=500),
    db: Session = Depends(get_db),
    driver=Depends(get_current_driver),
):
    events = (
        db.query(EleosEventHistory)
        .filter(EleosEventHistory.DriverCode == driver.Username)
        .order_by(EleosEventHistory.EventDt.desc())
        .limit(limit)
        .all()
    )
    return [EventHistoryItem.from_orm(event) for event in events]


@router.get("/stops", response_model=List[HistoryStopItem])
def list_history_stops(
    start: Optional[datetime] = Query(None),
    end: Optional[datetime] = Query(None),
    limit: int = Query(100, ge=1, le=1000),
    db: Session = Depends(get_db),
    driver=Depends(get_current_driver),
):
    query = db.query(EleosHistoryStopsByLoad).filter(
        EleosHistoryStopsByLoad.DriverUptID == driver.DriverID
    )

    if start:
        query = query.filter(EleosHistoryStopsByLoad.EventDatetime >= start)
    if end:
        query = query.filter(EleosHistoryStopsByLoad.EventDatetime <= end)

    stops = query.order_by(EleosHistoryStopsByLoad.EventDatetime.desc()).limit(limit).all()
    return [HistoryStopItem.from_orm(stop) for stop in stops]
