from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.vehicle_schema import VehicleCreate, VehicleResponse
from app.services.vehicle_service import create_vehicle_service, list_vehicles_service
from app.core.database import SessionLocal

router = APIRouter(prefix="/vehicles", tags=["Vehicles"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=VehicleResponse)
def create_vehicle(vehicle: VehicleCreate, db: Session = Depends(get_db)):
    return create_vehicle_service(db, vehicle)

@router.get("/", response_model=list[VehicleResponse])
def get_vehicles(db: Session = Depends(get_db)):
    return list_vehicles_service(db)