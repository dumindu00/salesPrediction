from sqlalchemy import Column, Integer, ForeignKey, Date, DECIMAL
from app.core.database import Base

class Sales(Base):
    __tablename__ = "sales"

    sale_id = Column(Integer, primary_key=True)
    vehicle_id = Column(Integer, ForeignKey("vehicles.vehicle_id"))
    quantity = Column(Integer)
    sale_date = Column(Date)
    unit_price_at_sale = Column(DECIMAL(10,2))
    total_sales = Column(DECIMAL(12,2))