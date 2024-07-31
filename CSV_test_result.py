"""
Test result class that outputs test results to a CSV file.
Tint: change the file path when you run the code.
"""
import pandas as pd

class CSVWriter:
    def __init__(self, file_path='C:\\Users\\Administrator\\calculator_project\\output.csv'):
        self.data = []  # List to store data
        self.file_path = file_path  # Path to the CSV file

    def add_row(self, description, result):
        """
        Adds a row of data to the list.
        """
        self.data.append((description, result))  # Append data to the list

    def write_to_csv(self):
        """
        Writes the data to the CSV file.
        """
        df = pd.DataFrame(self.data, columns=['Description', 'Result'])
        df.to_csv(self.file_path, index=False)

if __name__ == "__main__":
    # Create an instance of CSVWriter
    csv_writer = CSVWriter()

    # Add some data
    csv_writer.add_row("Test addition functionality: 2 + 2 should equal 4","4")
    csv_writer.add_row("Test subtraction functionality: 2 - 2 should equal 0","0")

    # Write the data to the CSV file
    csv_writer.write_to_csv()
