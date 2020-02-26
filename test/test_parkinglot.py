import unittest
import sys
sys.path.append("/home/user/Desktop/parkinglotmanagment/src")
from parkinglotmanagment import ParkingLot,Car


class ParkingLotManagment(unittest.TestCase):
    def test_givenCar_whenParkedInParkingLot_shouldBeReturnParked(self):
        car_object = Car()
        parkingLot_object = ParkingLot()
        result = parkingLot_object.placeVehicle(car_object)
        self.assertEqual(result,car_object)


    

if __name__ == "__main__":
    unittest.main()
