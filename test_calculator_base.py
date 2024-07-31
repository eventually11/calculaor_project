# test_calculator_base.py
import unittest
import csv
from calculator_base import CalculatorBase

class TestCalculatorBase(unittest.TestCase):
    def setUp(self):
        self.calculator = CalculatorBase()

    def test_addition(self):
        """Test addition functionality: 2 + 2 should equal 4."""
        result = self.calculator.evaluate_expression("2 + 2")
        self.assertEqual(result, "4")

    def test_subtraction(self):
        """Test subtraction functionality: 5 - 3 should equal 2."""
        result = self.calculator.evaluate_expression("5 - 3")
        self.assertEqual(result, "2")

    def test_multiplication(self):
        """Test multiplication functionality: 3 * 4 should equal 12."""
        result = self.calculator.evaluate_expression("3 * 4")
        self.assertEqual(result, "12")

    def test_division(self):
        """Test division functionality: 10 / 2 should equal 5."""
        result = self.calculator.evaluate_expression("10 / 2")
        self.assertIn(result, ["5", "5.0", "5.00"])

    def test_division_by_zero(self):
        """Test division by zero handling: 8 / 0 should return 'error'."""
        result = self.calculator.evaluate_expression("8 / 0")
        self.assertEqual(result, "error")

    def test_invalid_expression(self):
        """Test handling of invalid expression: 2 + should return 'error'."""
        result = self.calculator.evaluate_expression("2 +")
        self.assertEqual(result, "error")

    def test_complex_expression(self):
        """Test handling of complex expression: (2 + 3) * 4 should equal 20."""
        result = self.calculator.evaluate_expression("(2 + 3) * 4")
        self.assertEqual(result, "20")

class CSVTestResult(unittest.TextTestResult):
    def __init__(self, *args, file_path='C:\\Users\\Administrator\\calculator_project\\test_calculator_base_report.csv', **kwargs):
        super().__init__(*args, **kwargs)
        self.results = []
        self.file_path = file_path

    def addSuccess(self, test):
        super().addSuccess(test)
        self.results.append((test.shortDescription(), "success"))

    def addFailure(self, test, err):
        super().addFailure(test, err)
        self.results.append((test.shortDescription(), "failure"))

    def addError(self, test, err):
        super().addError(test, err)
        self.results.append((test.shortDescription(), "error"))

    def stopTestRun(self):
        super().stopTestRun()
        with open(self.file_path, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(['Expression', 'Result'])
            for expression, outcome in self.results:
                csv_writer.writerow([expression, outcome])

if __name__ == "__main__":
    test_loader = unittest.TestLoader()
    test_suite = test_loader.loadTestsFromTestCase(TestCalculatorBase)

    test_runner = unittest.TextTestRunner(resultclass=CSVTestResult)
    test_runner.run(test_suite)
