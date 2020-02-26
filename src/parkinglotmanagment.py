class Car:
    pass


class ParkingLot:
    def __init__(self, capacity=2):
        self.capacity = capacity
        self.parkingLot = []

    def placeVehicle(self, vehicle):
        self.parkingLot.append(vehicle)
        return vehicle
