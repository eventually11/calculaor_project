''' a simple calculator class that evaluates mathematical expressions.
This will output: 2 + 2 = 4
'''

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
    calculator = CalculatorBase()
    test_expression = "10 / 2"
    result = calculator.evaluate_expression(test_expression)
    print(f"Expression: {test_expression} = {result}")
