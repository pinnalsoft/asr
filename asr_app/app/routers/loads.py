from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..dependencies import get_current_driver, get_db
from ..models.eleos_current import (
    EleosCurrentLoadsByDriver,
    EleosCurrentProductInfoByLoad,
    EleosCurrentStopsByLoad,
    EleosCurrentVehicleByDriver,
    EleosDataBOLByProduct,
    EleosDocumentationLinksByLoad,
)
from ..schemas.load import (
    BOLInfo,
    DocumentLink,
    LoadDetail,
    LoadSummary,
    ProductInfo,
    StopInfo,
    VehicleInfo,
)

router = APIRouter(prefix="/loads", tags=["loads"])


@router.get("/", response_model=list[LoadSummary])
def list_loads(db: Session = Depends(get_db), driver=Depends(get_current_driver)):
    loads = (
        db.query(EleosCurrentLoadsByDriver)
        .filter(EleosCurrentLoadsByDriver.DriverID == driver.DriverID)
        .all()
    )
    vehicle = (
        db.query(EleosCurrentVehicleByDriver)
        .filter(EleosCurrentVehicleByDriver.DriverID == driver.DriverID)
        .first()
    )
    vehicle_schema = VehicleInfo.from_orm(vehicle) if vehicle else None

    response: list[LoadSummary] = []
    for load in loads:
        summary = LoadSummary.from_orm(load)
        summary.vehicle = vehicle_schema
        response.append(summary)
    return response


@router.get("/{order_id}", response_model=LoadDetail)
def load_detail(
    order_id: int, db: Session = Depends(get_db), driver=Depends(get_current_driver)
):
    load = (
        db.query(EleosCurrentLoadsByDriver)
        .filter(
            EleosCurrentLoadsByDriver.DriverID == driver.DriverID,
            EleosCurrentLoadsByDriver.OrderID == order_id,
        )
        .first()
    )
    if not load:
        raise HTTPException(status_code=404, detail="Load not found")

    vehicle = (
        db.query(EleosCurrentVehicleByDriver)
        .filter(EleosCurrentVehicleByDriver.DriverID == driver.DriverID)
        .first()
    )
    products = (
        db.query(EleosCurrentProductInfoByLoad)
        .filter(
            EleosCurrentProductInfoByLoad.DriverID == driver.DriverID,
            EleosCurrentProductInfoByLoad.OrderID == order_id,
        )
        .all()
    )
    stops = (
        db.query(EleosCurrentStopsByLoad)
        .filter(
            EleosCurrentStopsByLoad.DriverID == driver.DriverID,
            EleosCurrentStopsByLoad.OrderID == order_id,
        )
        .all()
    )
    documents = (
        db.query(EleosDocumentationLinksByLoad)
        .filter(
            EleosDocumentationLinksByLoad.OrderID == order_id,
            EleosDocumentationLinksByLoad.ShiftDetail == load.ShiftDetail,
        )
        .all()
    )
    bol_entries = (
        db.query(EleosDataBOLByProduct)
        .filter(
            EleosDataBOLByProduct.OrderID == order_id,
            EleosDataBOLByProduct.DriverID == driver.DriverID,
        )
        .all()
    )

    detail = LoadDetail.from_orm(load)
    detail.vehicle = VehicleInfo.from_orm(vehicle) if vehicle else None
    detail.products = [ProductInfo.from_orm(p) for p in products]
    detail.stops = [StopInfo.from_orm(s) for s in stops]
    detail.documents = [DocumentLink.from_orm(d) for d in documents]
    detail.bol = [BOLInfo.from_orm(b) for b in bol_entries]
    return detail


@router.get("/{order_id}/stops", response_model=list[StopInfo])
def load_stops(
    order_id: int, db: Session = Depends(get_db), driver=Depends(get_current_driver)
):
    stops = (
        db.query(EleosCurrentStopsByLoad)
        .filter(
            EleosCurrentStopsByLoad.DriverID == driver.DriverID,
            EleosCurrentStopsByLoad.OrderID == order_id,
        )
        .all()
    )
    return [StopInfo.from_orm(stop) for stop in stops]


@router.get("/{order_id}/bol", response_model=list[BOLInfo])
def load_bol(
    order_id: int, db: Session = Depends(get_db), driver=Depends(get_current_driver)
):
    bol_entries = (
        db.query(EleosDataBOLByProduct)
        .filter(
            EleosDataBOLByProduct.DriverID == driver.DriverID,
            EleosDataBOLByProduct.OrderID == order_id,
        )
        .all()
    )
    return [BOLInfo.from_orm(bol) for bol in bol_entries]


@router.get("/{order_id}/documents", response_model=list[DocumentLink])
def load_documents(
    order_id: int, db: Session = Depends(get_db), driver=Depends(get_current_driver)
):
    documents = (
        db.query(EleosDocumentationLinksByLoad)
        .join(
            EleosCurrentLoadsByDriver,
            (
                EleosDocumentationLinksByLoad.ShiftDetail
                == EleosCurrentLoadsByDriver.ShiftDetail
            )
            & (EleosDocumentationLinksByLoad.OrderID == EleosCurrentLoadsByDriver.OrderID),
        )
        .filter(
            EleosCurrentLoadsByDriver.DriverID == driver.DriverID,
            EleosCurrentLoadsByDriver.OrderID == order_id,
        )
        .all()
    )
    return [DocumentLink.from_orm(doc) for doc in documents]
