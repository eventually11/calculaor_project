'''test_calculator_base ,CSV_writer should be put in a same directory or folder
'''


import sys
import os
import unittest
import pandas as pd
from test_calculator_base import TestCalculatorBase
from CSV_writer import CSVWriter

class TestRunner:
    def __init__(self):
        # Add the current directory to sys.path
        current_dir = os.path.dirname(os.path.abspath(__file__)) if '__file__' in globals() else os.getcwd()
        sys.path.append(current_dir)

    def run(self):
        test_result = unittest.main(exit=False)
        # df = pd.DataFrame([{
        #     "Test Name": str(test),
        #     "Result": "Fail" if test_result.result.wasSuccessful() else "Pass",
        #     "Expected": "Pass",
        #     "Passed": test_result.result.wasSuccessful()
        # } for test in test_result.result.testsRun])
        # df.to_csv(os.path.join(os.path.dirname(__file__), 'test_calculator_base_report.csv'), index=False)
        return test_result

    

    # def run_tests(self):
    #     # Run the tests and get the results
    #     test_suite = unittest.TestLoader().loadTestsFromTestCase(TestCalculatorBase)
    #     test_result = unittest.TextTestRunner().run(test_suite)
        
    #     # Collect results
    #     results = []
    #     for test, err in test_result.failures + test_result.errors:
    #         results.append({
    #             "Test Name": str(test),
    #             "Result": "Fail",
    #             "Expected": "Pass",
    #             "Passed": False
    #         })
    #     for test in test_suite:
    #         if test not in [t[0] for t in test_result.failures + test_result.errors]:
    #             results.append({
    #                 "Test Name": str(test),
    #                 "Result": "Pass",
    #                 "Expected": "Pass",
    #                 "Passed": True
    #             })
    #     return results

    # def write_results_to_csv(self, results):
    #     # Convert results to DataFrame
    #     df = pd.DataFrame(results, columns=["Test Name", "Result", "Expected", "Passed"])

    #     # Create an instance of the CSV writer
    #     csv_writer = CSVWriter()

    #     # Add test results to the CSV writer
    #     for index, row in df.iterrows():
    #         csv_writer.add_row(row["Test Name"], row["Result"], row["Expected"], row["Passed"])

    #     # Write the test results to a CSV file
    #     csv_writer.write_to_csv()

    # def run(self):
    #     results = self.run_tests()
    #     self.write_results_to_csv(results)
    #     print("Test results have been written to the CSV file.")

if __name__ == "__main__":
    test_runner = TestRunner()
    df=test_runner.run()
    