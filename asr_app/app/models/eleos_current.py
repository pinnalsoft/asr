from sqlalchemy import Boolean, Column, Date, DateTime, Integer, Numeric, String, Text

from ..database import Base


class EleosCurrentLoadsByDriver(Base):
    __tablename__ = "EleosCurrentLoadsByDriver"

    ShiftDetail = Column(Integer, primary_key=True)
    OrderID = Column(Integer, primary_key=True)
    DriverID = Column(Integer, primary_key=True)
    ShiftHeaderNum = Column(Integer)
    Date = Column(Date)
    Shift = Column(String(10))
    DriverName = Column(String(100))
    ActiveOrder = Column(Boolean)
    OrderStatus = Column(String(20))
    LoadStatus = Column(String(20))
    TempLoadStatus = Column(String(20))
    LoadNum = Column(String(50))
    LoadNumOrd = Column(Integer)
    SupplierID = Column(Integer)
    Supplier = Column(String(200))
    CustomerID = Column(Integer)
    Customer = Column(String(200))
    ShipTo = Column(String(200))
    LoadingNumber = Column(String(100))
    SpecialInstructions = Column(Text)
    SentMailCounter = Column(Integer)
    WorkFlowCode = Column(String(50))
    EventDescription = Column(String(255))
    NextLoadToActive = Column(Boolean)


class EleosCurrentProductInfoByLoad(Base):
    __tablename__ = "EleosCurrentProductInfoByLoad"

    ShiftDetail = Column(Integer, primary_key=True)
    DriverID = Column(Integer, primary_key=True)
    OrderID = Column(Integer, primary_key=True)
    OrderProdID = Column(Integer, primary_key=True)
    ProductID = Column(Integer)
    Product = Column(String(200))
    ProductCode = Column(String(50))
    ProductCounter = Column(Integer)
    DispatchedQuantity = Column(Numeric(10, 2))
    SentMailCounter = Column(Integer)
    EventDescription = Column(String(255))
    Ullage = Column(Numeric(10, 2))
    RTHrs = Column(Numeric(6, 2))
    ROHrs = Column(Numeric(6, 2))


class EleosCurrentStopsByLoad(Base):
    __tablename__ = "EleosCurrentStopsByLoad"

    ShiftDetail = Column(Integer, primary_key=True)
    OrderID = Column(Integer, primary_key=True)
    DriverID = Column(Integer, primary_key=True)
    TerminalID = Column(Integer, primary_key=True)
    TerminalGeotabID = Column(String(100))
    TerminalName = Column(String(200))
    TerminalProvince = Column(String(100))
    TerminalCity = Column(String(100))
    TerminalPostalCode = Column(String(20))
    TerminalAddress = Column(String(255))
    TerminalLatitude = Column(Numeric(9, 6))
    TerminalLongitude = Column(Numeric(9, 6))
    StationID = Column(Integer)
    StationGeotabID = Column(String(100))
    StationNumber = Column(String(50))
    StationName = Column(String(200))
    StationProvince = Column(String(100))
    StationCity = Column(String(100))
    StationPostalCode = Column(String(20))
    StationAddress = Column(String(255))
    StationLatitude = Column(Numeric(9, 6))
    StationLongitude = Column(Numeric(9, 6))
    SentMailCounter = Column(Integer)
    EventDescription = Column(String(255))


class EleosCurrentVehicleByDriver(Base):
    __tablename__ = "EleosCurrentVehicleByDriver"

    ShiftDetail = Column(Integer, primary_key=True)
    DriverID = Column(Integer, primary_key=True)
    DriverName = Column(String(100))
    TruckID = Column(Integer)
    Truck = Column(String(100))
    TrailerID = Column(Integer)
    Trailer = Column(String(100))
    Comp1 = Column(Numeric(10, 2))
    Comp2 = Column(Numeric(10, 2))
    Comp3 = Column(Numeric(10, 2))
    Comp4 = Column(Numeric(10, 2))
    Comp5 = Column(Numeric(10, 2))
    Comp6 = Column(Numeric(10, 2))
    ReplacementUnit = Column(Boolean)
    YardID = Column(Integer)
    YardName = Column(String(200))
    YardProvince = Column(String(100))
    YardCity = Column(String(100))
    YardPostalCode = Column(String(20))
    YardAddress = Column(String(255))
    YardLatitude = Column(Numeric(9, 6))
    YardLongitude = Column(Numeric(9, 6))
    SentMailCounter = Column(Integer)
    EventDescription = Column(String(255))


class EleosDataBOLByProduct(Base):
    __tablename__ = "EleosDataBOLByProduct"

    ID = Column(Integer, primary_key=True, index=True)
    ShiftDetail = Column(Integer)
    DriverID = Column(Integer)
    OrderID = Column(Integer)
    OrderProdID = Column(Integer)
    ProductID = Column(Integer)
    ProductCounter = Column(Integer)
    Product = Column(String(200))
    ProductCode = Column(String(50))
    BOLNumber = Column(String(100))
    PlannedAmount = Column(Numeric(10, 2))
    GrossQuantity = Column(Numeric(10, 2))
    NetQuantity = Column(Numeric(10, 2))
    Ullage = Column(Numeric(10, 2))
    RTHrs = Column(Numeric(6, 2))
    ROHrs = Column(Numeric(6, 2))


class EleosDocumentationLinksByLoad(Base):
    __tablename__ = "EleosDocumentationLinksByLoad"

    ShiftDetail = Column(Integer, primary_key=True)
    OrderID = Column(Integer, primary_key=True)
    DocumentID = Column(Integer, primary_key=True)
    DocumentType = Column(String(50))
    UploadedAt = Column(DateTime)
    Link = Column(String(500))
