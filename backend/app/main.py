from fastapi import FastAPI
from app.api import routes_vehicle, routes_analytics

app = FastAPI()

app.include_router(routes_vehicle.router)
app.include_router(routes_analytics.router)

@app.get("/")
def root():
    return {"message": "Vehicle Sales API running"}