class Car:
    pass


class ParkingLot:
    def __init__(self, capacity=2):
        self.capacity = capacity
        self.parkingLot = []

    def placeVehicle(self, vehicle):
        self.parkingLot.append(vehicle)
        return vehicle

    def removeVehicle(self, vehicle):
        if vehicle == Car():
            vehicle = None

    def isFull(self):
        return len(self.parkingLot) == self.capacity


class ParkingLotOwner(ParkingLot):
    pass
