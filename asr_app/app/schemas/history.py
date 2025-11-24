from datetime import datetime
from decimal import Decimal
from typing import Optional
from pydantic import BaseModel


class EventHistory(BaseModel):
    event_id: int
    activity: Optional[str]
    event_dt: Optional[datetime]
    latitude: Optional[Decimal]
    longitude: Optional[Decimal]
    odometer: Optional[Decimal]
    fuel_level: Optional[Decimal]
    order_number: Optional[str]
    load_number: Optional[str]
    shift_number: Optional[str]
    stop_number: Optional[str]

    class Config:
        from_attributes = True


class HistoryStop(BaseModel):
    history_id: int
    event_datetime: Optional[datetime]
    activity: Optional[str]
    shift_detail: Optional[int]
    order_id: Optional[int]
    load_num: Optional[str]
    load_num_ord: Optional[int]
    driver_upt_id: Optional[int]
    driver_name: Optional[str]
    truck_upt_id: Optional[int]
    trailer_upt_id: Optional[int]
    stop_type: Optional[str]
    stop_upt_id: Optional[int]
    stop_geotab_id: Optional[str]
    stop_name: Optional[str]
    stop_latitude: Optional[Decimal]
    stop_longitude: Optional[Decimal]
    stop_odometer: Optional[Decimal]
    stop_fuel_level: Optional[Decimal]

    class Config:
        from_attributes = True

