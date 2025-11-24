from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .. import schemas
from ..dependencies import get_current_driver, get_db
from ..models.eleos_current import (
    EleosCurrentLoadsByDriver,
    EleosCurrentProductInfoByLoad,
    EleosCurrentStopsByLoad,
    EleosCurrentVehicleByDriver,
    EleosDataBOLByProduct,
    EleosDocumentationLinksByLoad,
)
from ..models.eleos_driver import EleosDriverCredentials

router = APIRouter(prefix="/loads", tags=["loads"])


def _vehicle_payload(vehicle):
    if not vehicle:
        return None
    return schemas.load.VehicleInfo(
        truck=vehicle.Truck,
        trailer=vehicle.Trailer,
        replacement_unit=vehicle.ReplacementUnit,
        yard_name=vehicle.YardName,
        yard_city=vehicle.YardCity,
        yard_province=vehicle.YardProvince,
        yard_postal_code=vehicle.YardPostalCode,
        yard_address=vehicle.YardAddress,
        yard_latitude=vehicle.YardLatitude,
        yard_longitude=vehicle.YardLongitude,
        comps={
            "comp1": vehicle.Comp1,
            "comp2": vehicle.Comp2,
            "comp3": vehicle.Comp3,
            "comp4": vehicle.Comp4,
            "comp5": vehicle.Comp5,
            "comp6": vehicle.Comp6,
        },
    )


@router.get("", response_model=List[schemas.load.CurrentLoad])
def list_loads(
    current_driver: EleosDriverCredentials = Depends(get_current_driver),
    db: Session = Depends(get_db),
):
    loads = (
        db.query(EleosCurrentLoadsByDriver)
        .filter(EleosCurrentLoadsByDriver.DriverID == current_driver.DriverID)
        .all()
    )
    vehicles_by_shift = {
        v.ShiftDetail: v
        for v in db.query(EleosCurrentVehicleByDriver)
        .filter(EleosCurrentVehicleByDriver.DriverID == current_driver.DriverID)
        .all()
    }
    response: List[schemas.load.CurrentLoad] = []
    for load in loads:
        response.append(
            schemas.load.CurrentLoad(
                shift_detail=load.ShiftDetail,
                date=load.Date,
                shift=load.Shift,
                order_id=load.OrderID,
                order_status=load.OrderStatus,
                load_status=load.LoadStatus,
                load_num=load.LoadNum,
                supplier=load.Supplier,
                customer=load.Customer,
                ship_to=load.ShipTo,
                loading_number=load.LoadingNumber,
                special_instructions=load.SpecialInstructions,
                work_flow_code=load.WorkFlowCode,
                next_load_to_active=load.NextLoadToActive,
                vehicle=_vehicle_payload(vehicles_by_shift.get(load.ShiftDetail)),
            )
        )
    return response


@router.get("/{order_id}", response_model=schemas.load.LoadDetail)
def load_detail(
    order_id: int,
    current_driver: EleosDriverCredentials = Depends(get_current_driver),
    db: Session = Depends(get_db),
):
    load = (
        db.query(EleosCurrentLoadsByDriver)
        .filter(
            EleosCurrentLoadsByDriver.OrderID == order_id,
            EleosCurrentLoadsByDriver.DriverID == current_driver.DriverID,
        )
        .first()
    )
    if not load:
        raise HTTPException(status_code=404, detail="Load not found")

    vehicle = (
        db.query(EleosCurrentVehicleByDriver)
        .filter(
            EleosCurrentVehicleByDriver.DriverID == current_driver.DriverID,
            EleosCurrentVehicleByDriver.ShiftDetail == load.ShiftDetail,
        )
        .first()
    )

    products = (
        db.query(EleosCurrentProductInfoByLoad)
        .filter(
            EleosCurrentProductInfoByLoad.OrderID == order_id,
            EleosCurrentProductInfoByLoad.DriverID == current_driver.DriverID,
        )
        .all()
    )

    stops = (
        db.query(EleosCurrentStopsByLoad)
        .filter(
            EleosCurrentStopsByLoad.OrderID == order_id,
            EleosCurrentStopsByLoad.DriverID == current_driver.DriverID,
        )
        .all()
    )

    return schemas.load.LoadDetail(
        shift_detail=load.ShiftDetail,
        date=load.Date,
        shift=load.Shift,
        order_id=load.OrderID,
        order_status=load.OrderStatus,
        load_status=load.LoadStatus,
        load_num=load.LoadNum,
        supplier=load.Supplier,
        customer=load.Customer,
        ship_to=load.ShipTo,
        loading_number=load.LoadingNumber,
        special_instructions=load.SpecialInstructions,
        work_flow_code=load.WorkFlowCode,
        next_load_to_active=load.NextLoadToActive,
        vehicle=_vehicle_payload(vehicle),
        products=[
            schemas.load.ProductInfo(
                order_prod_id=p.OrderProdID,
                product_id=p.ProductID,
                product=p.Product,
                product_code=p.ProductCode,
                product_counter=p.ProductCounter,
                dispatched_quantity=p.DispatchedQuantity,
                ullage=p.Ullage,
                rt_hrs=p.RTHrs,
                ro_hrs=p.ROHrs,
            )
            for p in products
        ],
        stops=[
            schemas.load.StopInfo(
                terminal_id=s.TerminalID,
                terminal_name=s.TerminalName,
                terminal_city=s.TerminalCity,
                terminal_province=s.TerminalProvince,
                terminal_address=s.TerminalAddress,
                terminal_latitude=s.TerminalLatitude,
                terminal_longitude=s.TerminalLongitude,
                station_id=s.StationID,
                station_number=s.StationNumber,
                station_name=s.StationName,
                station_city=s.StationCity,
                station_province=s.StationProvince,
                station_address=s.StationAddress,
                station_latitude=s.StationLatitude,
                station_longitude=s.StationLongitude,
            )
            for s in stops
        ],
    )


@router.get("/{order_id}/stops", response_model=List[schemas.load.StopInfo])
def load_stops(
    order_id: int,
    current_driver: EleosDriverCredentials = Depends(get_current_driver),
    db: Session = Depends(get_db),
):
    stops = (
        db.query(EleosCurrentStopsByLoad)
        .filter(
            EleosCurrentStopsByLoad.OrderID == order_id,
            EleosCurrentStopsByLoad.DriverID == current_driver.DriverID,
        )
        .all()
    )
    return [
        schemas.load.StopInfo(
            terminal_id=s.TerminalID,
            terminal_name=s.TerminalName,
            terminal_city=s.TerminalCity,
            terminal_province=s.TerminalProvince,
            terminal_address=s.TerminalAddress,
            terminal_latitude=s.TerminalLatitude,
            terminal_longitude=s.TerminalLongitude,
            station_id=s.StationID,
            station_number=s.StationNumber,
            station_name=s.StationName,
            station_city=s.StationCity,
            station_province=s.StationProvince,
            station_address=s.StationAddress,
            station_latitude=s.StationLatitude,
            station_longitude=s.StationLongitude,
        )
        for s in stops
    ]


@router.get("/{order_id}/bol", response_model=List[schemas.load.BOLInfo])
def load_bol(
    order_id: int,
    current_driver: EleosDriverCredentials = Depends(get_current_driver),
    db: Session = Depends(get_db),
):
    bol_records = (
        db.query(EleosDataBOLByProduct)
        .filter(
            EleosDataBOLByProduct.OrderID == order_id,
            EleosDataBOLByProduct.DriverID == current_driver.DriverID,
        )
        .all()
    )
    return [
        schemas.load.BOLInfo(
            id=b.ID,
            order_prod_id=b.OrderProdID,
            product_id=b.ProductID,
            product_counter=b.ProductCounter,
            product=b.Product,
            product_code=b.ProductCode,
            bol_number=b.BOLNumber,
            planned_amount=b.PlannedAmount,
            gross_quantity=b.GrossQuantity,
            net_quantity=b.NetQuantity,
            ullage=b.Ullage,
            rt_hrs=b.RTHrs,
            ro_hrs=b.ROHrs,
        )
        for b in bol_records
    ]


@router.get("/{order_id}/documents", response_model=List[schemas.load.DocumentationLink])
def load_documents(
    order_id: int,
    current_driver: EleosDriverCredentials = Depends(get_current_driver),
    db: Session = Depends(get_db),
):
    docs = (
        db.query(EleosDocumentationLinksByLoad)
        .filter(
            EleosDocumentationLinksByLoad.OrderID == order_id,
            EleosDocumentationLinksByLoad.ShiftDetail.in_(
                db.query(EleosCurrentLoadsByDriver.ShiftDetail)
                .filter(
                    EleosCurrentLoadsByDriver.OrderID == order_id,
                    EleosCurrentLoadsByDriver.DriverID == current_driver.DriverID,
                )
                .subquery()
            ),
        )
        .all()
    )
    return [
        schemas.load.DocumentationLink(
            document_id=d.DocumentID,
            document_type=d.DocumentType,
            uploaded_at=d.UploadedAt,
            link=d.Link,
        )
        for d in docs
    ]

