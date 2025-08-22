import unittest

# Import the vitals_ok function from your monitor.py module
from monitor import vitals_ok

class VitalsOkTest(unittest.TestCase):
    """
    Tests the vitals_ok function.
    """

    def test_all_vitals_normal(self):
        """
        Tests scenarios where all vital signs are within normal ranges.
        Should return True.
        """
        self.assertTrue(vitals_ok(98.6, 75, 95))
        self.assertTrue(vitals_ok(95.0, 60, 90))  # Lower boundaries
        self.assertTrue(vitals_ok(102.0, 100, 100)) # Upper boundaries

    def test_temperature_critical(self):
        """
        Tests scenarios where only temperature is out of range.
        Should return False.
        """
        # Temperature too high
        self.assertFalse(vitals_ok(103.0, 75, 95))
        # Temperature too low
        self.assertFalse(vitals_ok(94.0, 75, 95))

    def test_pulse_rate_critical(self):
        """
        Tests scenarios where only pulse rate is out of range.
        Should return False.
        """
        # Pulse rate too high
        self.assertFalse(vitals_ok(98.6, 101, 95))
        # Pulse rate too low
        self.assertFalse(vitals_ok(98.6, 59, 95))

    def test_spo2_critical(self):
        """
        Tests scenarios where only SpO2 is out of range.
        Should return False.
        """
        # SpO2 too low
        self.assertFalse(vitals_ok(98.6, 75, 89))

    def test_multiple_vitals_critical(self):
        """
        Tests scenarios where more than one vital sign is out of range.
        Should return False.
        """
        # Temperature and Pulse Rate critical
        self.assertFalse(vitals_ok(103.0, 110, 95))
        # All three vitals critical
        self.assertFalse(vitals_ok(103.0, 110, 88))
        # Temperature and SpO2 critical
        self.assertFalse(vitals_ok(103.0, 75, 88))

    def test_edge_cases_around_boundaries(self):
        """
        Tests values just inside and just outside the boundaries.
        """
        # Temp: Just outside high
        self.assertFalse(vitals_ok(102.0001, 75, 95))
        # Temp: Just inside low
        self.assertTrue(vitals_ok(95.0001, 75, 95))

        # Pulse: Just outside high
        self.assertFalse(vitals_ok(98.6, 100.0001, 95))
        # Pulse: Just inside low
        self.assertTrue(vitals_ok(98.6, 60, 95)) 
                                                     
        # SpO2: Just outside low
        self.assertFalse(vitals_ok(98.6, 75, 89.9999))


if __name__ == '__main__':
    unittest.main(verbosity=2) # verbosity=2 provides more detailed output for each test





