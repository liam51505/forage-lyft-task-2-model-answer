import unittest
from ..tire import CarriganTire, OctoprimeTire

class TestCarriganTire(unittest.TestCase):
    def test_needs_service_true(self):
        tire = CarriganTire([0.9, 0.1, 0.1, 0.1])
        self.assertTrue(tire.needs_service())

    def test_needs_service_false(self):
        tire = CarriganTire([0.8, 0.1, 0.1, 0.1])
        self.assertFalse(tire.needs_service())

class TestOctoprimeTire(unittest.TestCase):
    def test_needs_service_true(self):
        tire = OctoprimeTire([0.8, 0.8, 0.8, 0.7])
        self.assertTrue(tire.needs_service())

    def test_needs_service_false(self):
        tire = OctoprimeTire([0.5, 0.5, 0.5, 0.5])
        self.assertFalse(tire.needs_service())

if __name__ == '__main__':
    unittest.main()
