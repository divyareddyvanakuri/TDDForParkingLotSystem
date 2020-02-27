class Car:
    pass


class ParkingLot:
    def __init__(self):
        self.parkingLot = []
    def placeVehicle(self, vehicle):
        self.parkingLot.append(vehicle)
        return vehicle
