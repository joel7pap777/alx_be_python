import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Create a calculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_add(self):
        """Test the add method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-5, -5), -10)
        self.assertEqual(self.calc.add(0, 10), 10)

    def test_subtract(self):
        """Test the subtract method."""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(-5, -5), 0)
        self.assertEqual(self.calc.subtract(10, 0), 10)

    def test_multiply(self):
        """Test the multiply method."""
        self.assertEqual(self.calc.multiply(4, 5), 20)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(-4, -4), 16)
        self.assertEqual(self.calc.multiply(0, 100), 0)

    def test_divide(self):
        """Test the divide method."""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(9, 3), 3)
        self.assertEqual(self.calc.divide(-8, 2), -4)
        self.assertEqual(self.calc.divide(5, 0), None)  # division by zero
        self.assertEqual(self.calc.divide(0, 5), 0)

if __name__ == "__main__":
    unittest.main()
