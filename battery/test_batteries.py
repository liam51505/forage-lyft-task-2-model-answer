import unittest
from datetime import date, timedelta
from battery import SpindlerBattery, NubbinBattery

class TestSpindlerBattery(unittest.TestCase):
    def test_needs_service_true(self):
        last_service_date = date.today() - timedelta(days=731)
        battery = SpindlerBattery(last_service_date, date.today())
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        last_service_date = date.today() - timedelta(days=365)
        battery = SpindlerBattery(last_service_date, date.today())
        self.assertFalse(battery.needs_service())

class TestNubbinBattery(unittest.TestCase):
    def test_needs_service_true(self):
        last_service_date = date.today() - timedelta(days=1461)
        battery = NubbinBattery(last_service_date, date.today())
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        last_service_date = date.today() - timedelta(days=1000)
        battery = NubbinBattery(last_service_date, date.today())
        self.assertFalse(battery.needs_service())

if __name__ == '__main__':
    unittest.main()
