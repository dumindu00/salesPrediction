from pydantic import BaseModel

class VehicleCreate(BaseModel):
    model_number: str
    category: str
    brand: str
    model_name: str
    unit_price: float

class VehicleResponse(VehicleCreate):
    vehicle_id: int

    class Config:
        from_attributes = True