import unittest
import math
from main import calculate_pi


class TestPiCalculation(unittest.TestCase):
    """Test cases for the calculate_pi function."""
    
    def test_pi_to_5_digits(self):
        """Test that pi is calculated correctly to 5 decimal places."""
        calculated_pi = calculate_pi()
        expected_pi = 3.14159
        
        self.assertEqual(calculated_pi, expected_pi,
                        f"Expected {expected_pi}, but got {calculated_pi}")
    
    def test_pi_accuracy(self):
        """Test that calculated pi is very close to math.pi."""
        calculated_pi = calculate_pi()
        actual_pi = math.pi
        
        # Check that the difference is less than 0.00001 (5 decimal places)
        self.assertAlmostEqual(calculated_pi, actual_pi, places=5,
                              msg=f"Calculated pi {calculated_pi} is not accurate to 5 decimal places")
    
    def test_pi_type(self):
        """Test that the function returns a float."""
        result = calculate_pi()
        self.assertIsInstance(result, float,
                            f"Expected float, but got {type(result)}")
    
    def test_pi_range(self):
        """Test that pi is within the expected range."""
        calculated_pi = calculate_pi()
        
        # Pi should be between 3.14159 and 3.14160
        self.assertGreaterEqual(calculated_pi, 3.14159,
                               "Calculated pi is too small")
        self.assertLessEqual(calculated_pi, 3.14160,
                            "Calculated pi is too large")
    
    def test_pi_first_5_decimals(self):
        """Test that the first 5 decimal places match the known value."""
        calculated_pi = calculate_pi()
        calculated_str = f"{calculated_pi:.5f}"
        expected_str = "3.14159"
        
        self.assertEqual(calculated_str, expected_str,
                        f"Expected '{expected_str}', but got '{calculated_str}'")


if __name__ == "__main__":
    # Run the tests
    print("Testing Pi Calculation Function")
    print("=" * 50)
    unittest.main(verbosity=2)
