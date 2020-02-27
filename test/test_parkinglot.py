import unittest
import sys
sys.path.append("/home/user/Desktop/parkinglotmanagment/src")
from parkinglotmanagment import ParkingLot,Car,ParkingLotOwner


class ParkingLotManagment(unittest.TestCase):
    def test_givenCar_whenParkedInParkingLot_shouldBeReturnParked(self):
        parkingLot_object = ParkingLot(2,ParkingLotOwner())
        result = parkingLot_object.placeVehicle(Car())
        self.assertEqual(result,True)

    def test_givenCar_whenUnparkedFromParkingLot_shouldBeReturnUnparked(self):
        parkingLot_object = ParkingLot(2,ParkingLotOwner())
        parkingLot_object.placeVehicle(Car())
        result = parkingLot_object.removeVehicle(Car())
        self.assertEqual(result,None)

    def test_lotIsFull_ownerWantToKnow_shouldBeKeepFullSign(self):
        parkingLot_object = ParkingLot(2,ParkingLotOwner())
        parkingLot_object.placeVehicle(Car())
        parkingLot_object.placeVehicle(Car())
        result =  parkingLot_object.placeVehicle(Car())
        self.assertEqual(ParkingLotOwner().lotFullNotification(),result)


if __name__ == "__main__":
    unittest.main()