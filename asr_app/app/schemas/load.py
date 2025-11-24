from datetime import date, datetime
from typing import List, Optional

from pydantic import BaseModel, Field


class VehicleInfo(BaseModel):
    ShiftDetail: int
    DriverID: int
    DriverName: Optional[str]
    TruckID: Optional[int]
    Truck: Optional[str]
    TrailerID: Optional[int]
    Trailer: Optional[str]
    Comp1: Optional[float]
    Comp2: Optional[float]
    Comp3: Optional[float]
    Comp4: Optional[float]
    Comp5: Optional[float]
    Comp6: Optional[float]
    ReplacementUnit: Optional[bool]
    YardID: Optional[int]
    YardName: Optional[str]
    YardProvince: Optional[str]
    YardCity: Optional[str]
    YardPostalCode: Optional[str]
    YardAddress: Optional[str]
    YardLatitude: Optional[float]
    YardLongitude: Optional[float]

    class Config:
        orm_mode = True


class LoadSummary(BaseModel):
    ShiftDetail: int
    OrderID: int
    DriverID: int
    ShiftHeaderNum: Optional[int]
    Date: Optional[date]
    Shift: Optional[str]
    DriverName: Optional[str]
    ActiveOrder: Optional[bool]
    OrderStatus: Optional[str]
    LoadStatus: Optional[str]
    TempLoadStatus: Optional[str]
    LoadNum: Optional[str]
    LoadNumOrd: Optional[int]
    SupplierID: Optional[int]
    Supplier: Optional[str]
    CustomerID: Optional[int]
    Customer: Optional[str]
    ShipTo: Optional[str]
    LoadingNumber: Optional[str]
    SpecialInstructions: Optional[str]
    WorkFlowCode: Optional[str]
    EventDescription: Optional[str]
    NextLoadToActive: Optional[bool]
    vehicle: Optional[VehicleInfo]

    class Config:
        orm_mode = True


class ProductInfo(BaseModel):
    ShiftDetail: int
    DriverID: int
    OrderID: int
    OrderProdID: int
    ProductID: Optional[int]
    Product: Optional[str]
    ProductCode: Optional[str]
    ProductCounter: Optional[int]
    DispatchedQuantity: Optional[float]
    SentMailCounter: Optional[int]
    EventDescription: Optional[str]
    Ullage: Optional[float]
    RTHrs: Optional[float]
    ROHrs: Optional[float]

    class Config:
        orm_mode = True


class StopInfo(BaseModel):
    ShiftDetail: int
    OrderID: int
    DriverID: int
    TerminalID: int
    TerminalGeotabID: Optional[str]
    TerminalName: Optional[str]
    TerminalProvince: Optional[str]
    TerminalCity: Optional[str]
    TerminalPostalCode: Optional[str]
    TerminalAddress: Optional[str]
    TerminalLatitude: Optional[float]
    TerminalLongitude: Optional[float]
    StationID: Optional[int]
    StationGeotabID: Optional[str]
    StationNumber: Optional[str]
    StationName: Optional[str]
    StationProvince: Optional[str]
    StationCity: Optional[str]
    StationPostalCode: Optional[str]
    StationAddress: Optional[str]
    StationLatitude: Optional[float]
    StationLongitude: Optional[float]
    SentMailCounter: Optional[int]
    EventDescription: Optional[str]

    class Config:
        orm_mode = True


class BOLInfo(BaseModel):
    ID: int
    ShiftDetail: Optional[int]
    DriverID: Optional[int]
    OrderID: Optional[int]
    OrderProdID: Optional[int]
    ProductID: Optional[int]
    ProductCounter: Optional[int]
    Product: Optional[str]
    ProductCode: Optional[str]
    BOLNumber: Optional[str]
    PlannedAmount: Optional[float]
    GrossQuantity: Optional[float]
    NetQuantity: Optional[float]
    Ullage: Optional[float]
    RTHrs: Optional[float]
    ROHrs: Optional[float]

    class Config:
        orm_mode = True


class DocumentLink(BaseModel):
    ShiftDetail: int
    OrderID: int
    DocumentID: int
    DocumentType: Optional[str]
    UploadedAt: Optional[datetime]
    Link: Optional[str]

    class Config:
        orm_mode = True


class LoadDetail(LoadSummary):
    products: List[ProductInfo] = Field(default_factory=list)
    stops: List[StopInfo] = Field(default_factory=list)
    documents: List[DocumentLink] = Field(default_factory=list)
    bol: List[BOLInfo] = Field(default_factory=list)
