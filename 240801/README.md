# calculaor_project
This is a simple calculator application built with Tkinter for the GUI and includes unit tests to ensure the functionality of the calculator.The tests are written using the unittest framework and include coverage reporting.

# Table of Contents
Setup
Running the Application
Running the Unit Tests
Setup
Clone the Repository

First, you need to clone the repository. If you have not yet installed Git, you can download the ZIP file of the repository from GitHub and extract it.

sh
Copy code
git clone https://github.com/your-username/advanced-calculator.git
cd advanced-calculator

Download python or Ananconda

# Running the Application
To run the application, you can use the following command. The application also accepts an optional command-line parameter to set the initial equation.

python main.py --equation "2+2"

# Running Tests
python calculator_test.py --report <path_to_save_report> --coverage-dir <path_to_save_coverage_report>
After running the tests, a CSV report of the test results will be saved to the specified path. Additionally, an HTML coverage report will be generated in the specified directory.

# Requirements
Python 3.6+
Tkinter (usually included with Python)
pandas
coverage
argparse


# Directory Structure
advanced-calculator/
│
├── calculator.py
├── calculator_test.py
├── README.md
└── requirements.txt