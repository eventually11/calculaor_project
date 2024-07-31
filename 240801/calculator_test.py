import unittest
import coverage
import tkinter as tk
from calculator import AdvancedCalculatorApp
import pandas as pd
import argparse

class TestAdvancedCalculatorApp(unittest.TestCase):
    # Class attributes for storing test results, report paths
    test_results = []
    report_path = "C:\\Users\\Administrator\\calculator_project\\test_report.csv"
    coverage_report_dir = "C:\\Users\\Administrator\\calculator_project\\coverage_html_report"

    def setUp(self):
        """Set up the test environment, create the Tkinter root and the calculator app instance."""
        self.root = tk.Tk()
        self.app = AdvancedCalculatorApp(self.root)

    def tearDown(self):
        """Destroy the Tkinter root after each test."""
        self.root.destroy()

    def simulate_clicks(self, clicks):
        """Simulate button clicks on the calculator."""
        for click in clicks:
            self.app.click(click)
            print(f"Clicked: {click}")

    @classmethod
    def log_result(cls, test_name, expected, actual, passed):
        """Log the result of a test."""
        cls.test_results.append({
            'Test Name': test_name,
            'Expected Result': expected,
            'Actual Result': actual,
            'Passed': passed
        })

    def test_addition(self):
        """Test addition functionality: 2 + 2 should equal 4."""
        self.simulate_clicks(list('2+2='))
        actual_result = self.app.equation.get()
        expected_result = '4'
        passed = actual_result == expected_result
        self.log_result('Addition', expected_result, actual_result, passed)
        print(f"Testing '2+2=': Expected result is 4, Actual result is '{actual_result}'")
        self.assertEqual(actual_result, '4')

    def test_multiplication(self):
        """Test multiplication functionality: 5 * 5 should equal 25."""
        self.simulate_clicks(list('5*5='))
        actual_result = self.app.equation.get()
        expected_result = '25'
        passed = actual_result == expected_result
        self.log_result('Multiplication', expected_result, actual_result, passed)
        print(f"Testing '5*5=': Expected result is 25, Actual result is '{actual_result}'")
        self.assertEqual(actual_result, '25')

    def test_invalid_operation(self):
        """Test invalid operation handling: 3++4 should return 'error' or '7'."""
        self.simulate_clicks(list('3++4='))
        actual_result = self.app.equation.get()
        expected_behavior = "Calculator may not handle invalid operations correctly yet."
        passed = actual_result in ['error', '7']
        self.log_result('Invalid Operation', 'error or 7', actual_result, passed)
        print(f"Testing '3++4=': Observed behavior is '{actual_result}'. {expected_behavior}")
        self.assertTrue(actual_result in ['error', '7'], "Unexpected result for invalid operation")

    def test_combined_operations(self):
        """Test combined operations: 6 - 2 + 3 should equal 7."""
        self.simulate_clicks(list('6-2+3='))
        actual_result = self.app.equation.get()
        expected_result = '7'
        passed = actual_result == expected_result
        self.log_result('Combined Operations', expected_result, actual_result, passed)
        print(f"Testing '6-2+3=': Expected result is 7, Actual result is '{actual_result}'")
        self.assertEqual(actual_result, '7')

    def test_clear(self):
        """Test clear functionality: 1 + 1 C should clear the input."""
        self.simulate_clicks(['1', '+', '1', 'C'])
        actual_result = self.app.equation.get()
        expected_result = ''
        passed = actual_result == expected_result
        self.log_result('Clear', expected_result, actual_result, passed)
        print(f"Testing clear: Expected result is empty, Actual result is '{actual_result}'")
        self.assertEqual(actual_result, '')

    def test_division_by_zero(self):
        """Test division by zero handling: 8 / 0 should return 'error'."""
        self.simulate_clicks(list('8/0='))
        actual_result = self.app.equation.get()
        expected_result = 'error'
        passed = actual_result == expected_result
        self.log_result('Division by Zero', expected_result, actual_result, passed)
        print(f"Testing '8/0=': Expected result is 'error', Actual result is '{actual_result}'")
        self.assertEqual(actual_result, 'error')

    @classmethod
    def tearDownClass(cls):
        """Generate a CSV report of the test results after all tests have run."""
        df = pd.DataFrame(cls.test_results)
        df.to_csv(cls.report_path, index=False)
        print(f"Test report saved to '{cls.report_path}'")

def main():
    parser = argparse.ArgumentParser(description="Run unit tests for the Advanced Calculator.")
    parser.add_argument("--report", type=str, default=TestAdvancedCalculatorApp.report_path, help="Path to save the test report CSV.")
    parser.add_argument("--coverage-dir", type=str, default=TestAdvancedCalculatorApp.coverage_report_dir, help="Directory to save the coverage report.")
    args = parser.parse_args()

    # Update the class attributes with the provided arguments
    TestAdvancedCalculatorApp.report_path = args.report
    TestAdvancedCalculatorApp.coverage_report_dir = args.coverage_dir

    # Start coverage measurement
    cov = coverage.Coverage()
    cov.start()

    # Load and run the test suite
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAdvancedCalculatorApp)
    unittest.TextTestRunner(verbosity=2).run(suite)

    # Stop coverage measurement
    cov.stop()
    cov.save()

    # Generate coverage report
    cov.html_report(directory=TestAdvancedCalculatorApp.coverage_report_dir)
    print(f"Coverage report saved to '{TestAdvancedCalculatorApp.coverage_report_dir}/index.html'")

if __name__ == '__main__':
    main()
