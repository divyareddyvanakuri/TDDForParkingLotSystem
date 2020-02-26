import unittest
import sys
sys.path.append("/home/user/Desktop/parkinglotmanagment/src")
from parkinglotmanagment import ParkingLot,Car,ParkingLotOwner


class ParkingLotManagment(unittest.TestCase):
    def test_givenCar_whenParkedInParkingLot_shouldBeReturnParked(self):
        car_object = Car()
        parkingLot_object = ParkingLot()
        result = parkingLot_object.placeVehicle(car_object)
        self.assertEqual(result,car_object)

    def test_givenCar_whenUnparkedFromParkingLot_shouldBeReturnUnparked(self):
        car_object = Car()
        parkingLot_object = ParkingLot()
        parkingLot_object.placeVehicle(car_object)
        result = parkingLot_object.removeVehicle(car_object)
        self.assertEqual(result,None)

    def test_lotIsFull_ownerWantToKnow_shouldBeReturnFull(self):
        car_object = Car()
        owner_object = ParkingLotOwner()
        owner_object.placeVehicle(car_object)
        owner_object.placeVehicle(car_object)
        result = owner_object.isFull()
        self.assertEqual(result,True)

    

if __name__ == "__main__":
    unittest.main()
