'''This script ensures that the CalculatorBase class is thoroughly 
tested and that any issues are documented 
and easily accessible through the generated CSV report.
'''



import unittest
import pandas as pd
import os
from calculator_base import CalculatorBase

class TestCalculatorBase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.results = []

    def setUp(self):
        self.calculator = CalculatorBase()

    def add_result(self, test_name, result, expected):
        self.__class__.results.append({
            "Test Name": test_name,
            "Result": result,
            "Expected": expected,
            "Passed": result == expected
        })

    def test_addition(self):
        """Test addition functionality: 2 + 2 should equal 4."""
        result = self.calculator.evaluate_expression("2 + 2")
        expected = "4"
        self.add_result("test_addition", result, expected)
        self.assertEqual(result, expected)

    def test_subtraction(self):
        """Test subtraction functionality: 5 - 3 should equal 2."""
        result = self.calculator.evaluate_expression("5 - 3")
        expected = "2"
        self.add_result("test_subtraction", result, expected)
        self.assertEqual(result, expected)

    def test_multiplication(self):
        """Test multiplication functionality: 3 * 4 should equal 12."""
        result = self.calculator.evaluate_expression("3 * 4")
        expected = "12"
        self.add_result("test_multiplication", result, expected)
        self.assertEqual(result, expected)

    def test_division(self):
        """Test division functionality: 10 / 2 should equal 5."""
        result = self.calculator.evaluate_expression("10 / 2")
        self.assertIn(result, ["5", "5.0", "5.00"])

    def test_division_by_zero(self):
        """Test division by zero handling: 8 / 0 should return 'error'."""
        result = self.calculator.evaluate_expression("8 / 0")
        expected = "error"
        self.add_result("test_division_by_zero", result, expected)
        self.assertEqual(result, expected)

    def test_invalid_expression(self):
        """Test handling of invalid expression: 2 + should return 'error'."""
        result = self.calculator.evaluate_expression("2 +")
        expected = "error"
        self.add_result("test_invalid_expression", result, expected)
        self.assertEqual(result, expected)

    def test_complex_expression(self):
        """Test handling of complex expression: (2 + 3) * 4 should equal 20."""
        result = self.calculator.evaluate_expression("(2 + 3) * 4")
        expected = "20"
        self.add_result("test_complex_expression", result, expected)
        self.assertEqual(result, expected)

    @classmethod
    def tearDownClass(cls):
        df = pd.DataFrame(cls.results)
        current_dir = os.path.dirname(os.path.abspath(__file__))
        csv_path = os.path.join(current_dir, 'test_calculator_base_report.csv')
        df.to_csv(csv_path, index=False)
        print(df)
        return df

if __name__ == "__main__":
    unittest.main()