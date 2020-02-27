class Car:
    pass


class ParkingLot:
    def __init__(self):
        self.parkingLot = []

    def placeVehicle(self, vehicle):
        self.parkingLot.append(vehicle)
        return vehicle

    def removeVehicle(self, vehicle):
        if vehicle == Car():
            vehicle = None
