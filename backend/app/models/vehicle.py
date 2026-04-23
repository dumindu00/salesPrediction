from sqlalchemy import Column, Integer, String, Enum, DECIMAL
from app.core.database import Base

class Vehicle(Base):
    __tablename__ = "vehicles"

    vehicle_id = Column(Integer, primary_key=True, index=True)
    model_number = Column(String(100), unique=True)
    category = Column(Enum('SUV', 'CAR', 'BIKE'))
    brand = Column(String(100))
    model_name = Column(String(100))
    unit_price = Column(DECIMAL(10,2))