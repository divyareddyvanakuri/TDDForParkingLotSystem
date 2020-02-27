from abc import ABC,abstractmethod

class Car:
    pass

class ParkingLot:
    def __init__(self,capacity,owner,security):
        self.parkingLot = [None]*capacity
        self.owner = owner
        self.security = security
        self.listOf_notifiers = [self.owner,self.security]

    def placeVehicle(self, vehicle):
        for index in range(len(self.parkingLot)):
            if self.parkingLot[index] == None:
                self.parkingLot[index] = vehicle
                return True
        for notifier in self.listOf_notifiers:
            notifier.lotFullNotification()
        return False


    def removeVehicle(self, vehicle):
        for index in range(len(self.parkingLot)):
            if self.parkingLot[index] == vehicle:
                self.parkingLot[index] = None
                self.owner.lotFreeNotification(index)
            return True


class ParkingLotObserver(ABC):

    def lotFullNotification(self):
        return False


class ParkingLotOwner(ParkingLotObserver):
    def __init__(self):
        super().__init__()



class ParkingLotSecurity(ParkingLotObserver):
    def __init__(self):
        super().__init__()

        