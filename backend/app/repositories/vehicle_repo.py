from sqlalchemy.orm import Session
from app.models.vehicle import Vehicle

def create_vehicle(db: Session, vehicle_data):
    vehicle = Vehicle(**vehicle_data.dict())
    db.add(vehicle)
    db.commit()
    db.refresh(vehicle)
    return vehicle

def get_all_vehicles(db: Session):
    return db.query(Vehicle).all()