from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.services.analytics_service import get_quarterly_profit
from app.core.database import SessionLocal

router = APIRouter(prefix="/analytics", tags=["Analytics"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/quarterly-profit")
def quarterly_profit(db: Session = Depends(get_db)):
    return get_quarterly_profit(db)