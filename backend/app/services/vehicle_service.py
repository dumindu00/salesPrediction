from app.repositories import vehicle_repo

def create_vehicle_service(db, vehicle_data):
    # you can add validation logic here
    return vehicle_repo.create_vehicle(db, vehicle_data)

def list_vehicles_service(db):
    return vehicle_repo.get_all_vehicles(db)