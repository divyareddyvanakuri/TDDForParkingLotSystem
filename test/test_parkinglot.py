import unittest
import sys
sys.path.append("/home/user/Desktop/parkinglotmanagment/src")
from parkinglotmanagment import ParkingLot,Car,ParkingLotOwner,ParkingLotSecurity


class ParkingLotManagment(unittest.TestCase):
    def test_givenCar_whenParkedInParkingLot_shouldBeReturnParked(self):
        parkingLot_object = ParkingLot(2,ParkingLotOwner(),ParkingLotSecurity())
        result = parkingLot_object.placeVehicle(Car())
        self.assertEqual(result,True)

    def test_givenCar_whenUnparkedFromParkingLot_shouldBeReturnUnparked(self):
        parkingLot_object = ParkingLot(2,ParkingLotOwner(),ParkingLotSecurity())
        parkingLot_object.placeVehicle(Car())
        result = parkingLot_object.removeVehicle(Car())
        self.assertEqual(result,True)

    def test_lotIsFull_ownerWantToKnow_shouldBeKeepFullSign(self):
        parkingLot_object = ParkingLot(2,ParkingLotOwner(),ParkingLotSecurity())
        parkingLot_object.placeVehicle(Car())
        parkingLot_object.placeVehicle(Car())
        result =  parkingLot_object.placeVehicle(Car())
        self.assertEqual(ParkingLotOwner().lotFullNotification(),result)

    def test_whenLotIsFull_securityWantToRedirectToStaff_shouldBeReturnRedirected(self):
        parkingLot_object = ParkingLot(2,ParkingLotOwner(),ParkingLotSecurity())
        parkingLot_object.placeVehicle(Car())
        parkingLot_object.placeVehicle(Car())
        result =  parkingLot_object.placeVehicle(Car())
        self.assertEqual(ParkingLotSecurity().lotFullNotification(),result)

    def test_lotIsFree_ownerWantToKnow_shouldBeTakeOutFullSign(self):
        parkingLot_object = ParkingLot(2,ParkingLotOwner(),ParkingLotSecurity())
        parkingLot_object.placeVehicle(Car())
        parkingLot_object.placeVehicle(Car())
        result = parkingLot_object.removeVehicle(Car())
        self.assertEqual(ParkingLotOwner().lotFreeNotification(),result)
    
        
if __name__ == "__main__":
    unittest.main()