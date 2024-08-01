"""
Test result class that outputs test results to a CSV file.
Tint: change the file path when you run the code.
"""
import pandas as pd

class CSVWriter:
    def __init__(self, file_path='C:\\Users\\Administrator\\calculator_project\\output.csv'):
        self.data = []  # List to store data
        self.file_path = file_path  # Path to the CSV file

    def add_row(self, description, result, expected, passed):
        """
        Adds a row of data to the list.
        """
        self.data.append((description, result, expected, passed))  # Append data to the list

    def write_to_csv(self):
        """
        Writes the data to the CSV file.
        """
        df = pd.DataFrame(self.data, columns=["Test Name", "Result", "Expected", "Passed"])
        df.to_csv(self.file_path, index=False)

if __name__ == "__main__":
    # Create an instance of CSVWriter
    csv_writer = CSVWriter()

    # Add some data
    csv_writer.add_row("test_addition", "4", "4", True)
    csv_writer.add_row("test_complex_expression", "20", "20", True)
    csv_writer.add_row("test_division_by_zero", "error", "error", True)
    csv_writer.add_row("test_invalid_expression", "error", "error", True)
    csv_writer.add_row("test_multiplication", "12", "12", True)
    csv_writer.add_row("test_subtraction", "2", "2", True)

    # Write the data to the CSV file
    csv_writer.write_to_csv()