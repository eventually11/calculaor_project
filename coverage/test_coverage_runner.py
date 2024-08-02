''' you can use it with any test suite or test case class without changing the code.
just change the imported library and the test case class name in the code.
 '''


import os
import coverage
import unittest
from test_calculator_base import TestCalculatorBase  # Flexiable，suit for the different file path

class TestCoverageRunner:
    def __init__(self, test_case_class, report_dir='htmlcov'):
        # Determine the directory of the current script
        script_dir = os.path.dirname(os.path.abspath(__file__))
        # Set the report directory to be within the script's directory
        self.report_dir = os.path.join(script_dir, report_dir)
        self.cov = coverage.Coverage()
        self.test_case_class = test_case_class

    def start_coverage(self):
        """Start coverage measurement."""
        self.cov.start()

    def run_tests(self):
        """Run tests from the provided test case class."""
        suite = unittest.TestSuite()
        suite.addTest(unittest.makeSuite(self.test_case_class))
        runner = unittest.TextTestRunner()
        runner.run(suite)

    def stop_coverage(self):
        """Stop coverage measurement and save data."""
        self.cov.stop()
        self.cov.save()

    def generate_reports(self):
        """Generate coverage reports."""
        self.cov.report()
        self.cov.html_report(directory=self.report_dir)
        print(f"HTML coverage report generated in '{self.report_dir}' directory")

    def execute(self):
        """Execute the full coverage and test run process."""
        self.start_coverage()
        self.run_tests()
        self.stop_coverage()
        self.generate_reports()

# Example usage:
if __name__ == '__main__':
    runner = TestCoverageRunner(test_case_class=TestCalculatorBase, report_dir='htmlcov')
    runner.execute()