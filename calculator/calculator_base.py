''' a simple calculator class that evaluates mathematical expressions.
This will output: 2 + 2 = 4
'''
    # To run this script from the command line:
    # 1. Open a terminal or command prompt.
    # 2. Navigate to the directory containing this script.
    # 3. Run the script using the command: python calculator_base.py --equation "2+2"

import argparse

# calculator_base.py
class CalculatorBase:
    def __init__(self):
        pass

    def evaluate_expression(self, expression):
        try:
            result = str(eval(expression))
            print(f"Evaluating: {expression} = {result}")
            return result
        except Exception as e:
            print(f"Error evaluating: {expression}, Error: {e}")
            return "error"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Evaluate a mathematical expression.')
    parser.add_argument('--equation', type=str, required=True, help='The mathematical expression to evaluate')
    args = parser.parse_args()

    calculator = CalculatorBase()
    result = calculator.evaluate_expression(args.equation)
    print(f"Expression: {args.equation} = {result}")

