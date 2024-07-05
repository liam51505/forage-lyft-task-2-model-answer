import unittest
from engine import CapuletEngine, SternmanEngine, WilloughbyEngine

class TestCapuletEngine(unittest.TestCase):
    def test_needs_service_true(self):
        engine = CapuletEngine(0, 30000)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        engine = CapuletEngine(30000, 50000)
        self.assertFalse(engine.needs_service())

class TestSternmanEngine(unittest.TestCase):
    def test_needs_service_true(self):
        engine = SternmanEngine(warning_light_on=True)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        engine = SternmanEngine(warning_light_on=False)
        self.assertFalse(engine.needs_service())

class TestWilloughbyEngine(unittest.TestCase):
    def test_needs_service_true(self):
        engine = WilloughbyEngine(0, 60000)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        engine = WilloughbyEngine(60000, 90000)
        self.assertFalse(engine.needs_service())

if __name__ == '__main__':
    unittest.main()
