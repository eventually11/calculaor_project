'''This script defines an AdvancedCalculatorApp class that extends CalculatorBase and uses tkinter to 
create a graphical user interface for a calculator. It initializes the main window,
 sets up an entry widget for user input, and binds it to a StringVar to hold the equation.
 '''


import tkinter as tk
import argparse
from calculator_base import CalculatorBase

class AdvancedCalculatorApp(CalculatorBase):
    def __init__(self, master, initial_equation=""):
        super().__init__()  # Initialize the CalculatorBase
        # Initialize the main window
        self.master = master
        master.title("Advanced Calculator")

        # Create a StringVar to hold the equation
        self.equation = tk.StringVar(value=initial_equation)
        
        # Create an entry widget for user input and bind it to the equation StringVar
        self.input_field = tk.Entry(master, textvariable=self.equation)
        self.input_field.grid(row=0, column=0, columnspan=4, sticky="nsew")

        # Create calculator buttons
        self.create_buttons()

    def create_buttons(self):
        # Define the buttons layout
        buttons = [
            '7', '8', '9', '+',
            '4', '5', '6', '-',
            '1', '2', '3', '*',
            'C', '0', '=', '/'
        ]

        row = 1
        col = 0
        # Create and place buttons in the grid
        for button in buttons:
            tk.Button(self.master, text=button, command=lambda b=button: self.click(b)).grid(row=row, column=col, sticky="nsew")
            col += 1
            if col > 3:
                col = 0
                row += 1

        # Adjust column and row weights to make buttons expand
        for i in range(4):
            self.master.grid_columnconfigure(i, weight=1)
            self.master.grid_rowconfigure(i+1, weight=1)

    def click(self, button):
        # Get the current equation from the entry field
        current_equation = self.equation.get()
        if button == '=':
            try:
                # Evaluate the equation and display the result
                self.equation.set(str(eval(current_equation)))
            except Exception as e:
                # If there is an error, display "error" in the entry field
                self.equation.set("error")
        elif button == 'C':
            # Clear the entry field
            self.equation.set("")
        else:
            # Append the clicked button's text to the current input
            self.equation.set(current_equation + button)

    @classmethod
    def from_command_line(cls, master):
        """Parse command line arguments and create an instance of the class."""
        parser = argparse.ArgumentParser(description="Advanced Calculator")
        parser.add_argument("--equation", type=str, help="Initial equation to display", default="")
        args = parser.parse_args()
        return cls(master, initial_equation=args.equation)

if __name__ == "__main__":
    # Create the main window and run the application
    root = tk.Tk()
    app = AdvancedCalculatorApp.from_command_line(root)
    root.mainloop()