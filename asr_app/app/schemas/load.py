from datetime import date, datetime
from decimal import Decimal
from pydantic import BaseModel
from typing import List, Optional


class VehicleInfo(BaseModel):
    truck: Optional[str]
    trailer: Optional[str]
    replacement_unit: Optional[bool]
    yard_name: Optional[str]
    yard_city: Optional[str]
    yard_province: Optional[str]
    yard_postal_code: Optional[str]
    yard_address: Optional[str]
    yard_latitude: Optional[Decimal]
    yard_longitude: Optional[Decimal]
    comps: dict[str, Optional[Decimal]]

    class Config:
        from_attributes = True


class CurrentLoad(BaseModel):
    shift_detail: int
    date: Optional[date]
    shift: Optional[str]
    order_id: Optional[int]
    order_status: Optional[str]
    load_status: Optional[str]
    load_num: Optional[str]
    supplier: Optional[str]
    customer: Optional[str]
    ship_to: Optional[str]
    loading_number: Optional[str]
    special_instructions: Optional[str]
    work_flow_code: Optional[str]
    next_load_to_active: Optional[bool]
    vehicle: Optional[VehicleInfo] = None

    class Config:
        from_attributes = True


class ProductInfo(BaseModel):
    order_prod_id: int
    product_id: Optional[int]
    product: Optional[str]
    product_code: Optional[str]
    product_counter: Optional[int]
    dispatched_quantity: Optional[Decimal]
    ullage: Optional[Decimal]
    rt_hrs: Optional[Decimal]
    ro_hrs: Optional[Decimal]

    class Config:
        from_attributes = True


class StopInfo(BaseModel):
    terminal_id: Optional[int]
    terminal_name: Optional[str]
    terminal_city: Optional[str]
    terminal_province: Optional[str]
    terminal_address: Optional[str]
    terminal_latitude: Optional[Decimal]
    terminal_longitude: Optional[Decimal]
    station_id: Optional[int]
    station_number: Optional[str]
    station_name: Optional[str]
    station_city: Optional[str]
    station_province: Optional[str]
    station_address: Optional[str]
    station_latitude: Optional[Decimal]
    station_longitude: Optional[Decimal]

    class Config:
        from_attributes = True


class BOLInfo(BaseModel):
    id: int
    order_prod_id: Optional[int]
    product_id: Optional[int]
    product_counter: Optional[int]
    product: Optional[str]
    product_code: Optional[str]
    bol_number: Optional[str]
    planned_amount: Optional[Decimal]
    gross_quantity: Optional[Decimal]
    net_quantity: Optional[Decimal]
    ullage: Optional[Decimal]
    rt_hrs: Optional[Decimal]
    ro_hrs: Optional[Decimal]

    class Config:
        from_attributes = True


class DocumentationLink(BaseModel):
    document_id: int
    document_type: Optional[str]
    uploaded_at: Optional[datetime]
    link: Optional[str]

    class Config:
        from_attributes = True


class LoadDetail(CurrentLoad):
    products: List[ProductInfo] = []
    stops: List[StopInfo] = []

