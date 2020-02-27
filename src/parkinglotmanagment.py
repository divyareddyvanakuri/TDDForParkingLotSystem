from abc import ABC,abstractmethod

class Car:
    pass

class ParkingLot:
    def __init__(self,capacity,owner):
        self.parkingLot = [None]*capacity
        self.owner = owner

    def placeVehicle(self, vehicle):
        for index in range(len(self.parkingLot)):
            if self.parkingLot[index] == None:
                self.parkingLot[index] = vehicle
                return True
        self.owner.lotFullNotification()
        return False

    def removeVehicle(self, vehicle):
        if vehicle == Car():
            vehicle = None
    

class ParkingLotOwner:

    def lotFullNotification(self):
        return False

        