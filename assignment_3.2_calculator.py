'''
Assignment 3.2: Creating a simple pocket calculator
Author: Paul Ring
github link: https://github.com/plr5034/Python_ADD-160/blob/main/assignment_3.2_calculator.py

Create a very simple and very specific calculator that contains two entry
fields that the user can use to enter arguments, radio buttons to select the
operation to perform and a button to initiate the evaluation.

Objectives
 - Use the following widgets
    * Entry
    * Radiobutton
    * Button

 - Manage widgets with the grid manager
 - Check the validity of user input and handle errors

Expectation for the calculator behavior:

 - If both (entry) fields contain valid (integer or float) numbers, clicking the 
Evaluate button should display an info window showing the evaluation's result

 - If any of the fields contains invalid data (e.g., a string, or a field
is empty), clicking the Evaluate button should present an error window
describing the problem, and the focus should be moved to the field causing
the problem.
 - Don't forget to protect your code from dividing by zero, and use the
grid manager to compose the window interior.

'''

# Import the necessary libraries
import tkinter as tk
from tkinter import messagebox
import platform # needed to check the OS for windows width

def operate():
    '''
    Function to perform the selected arithmetic operation.
    
    It retrieves the selected operator from the radio buttons and calls
    the corresponding function to perform the appropriate operation.

    Aargs:
        None
    Returns:
        None
    '''
    operator= current_operator.get()  # Get the selected operator from the radio buttons
    print(f"Selected operator: {operator}")  # Debugging print statement
    if operator == "add_nums":
        add_numbers()
    elif operator == "subtract_nums":
        subtract_numbers()
    elif operator == "multiply_nums":
        multiply_numbers()
    elif operator == "divide_nums":
        divide_numbers()

def add_numbers():
    '''
    Function to add two numbers entered in the entry fields.
    
    It retrieves the numbers from the entry fields and if valid, performs
    the addition operation. If invalid input is detected, it shows an error
    message box.

    Args:
        None
    Returns:
        None
    
    '''
    try:
        num1 = float(entry_operand1.get())
        num2 = float(entry_operand2.get())
        result = num1 + num2
        tk.messagebox.showinfo("Result", f"The result is: {result}")
    except ValueError:
        tk.messagebox.showerror("Input Error", "Please enter valid numbers.")

def subtract_numbers():
    '''
     Function to subtract two numbers entered in the entry fields.
    
    It retrieves the numbers from the entry fields and if valid, performs
    the subtraction operation. If invalid input is detected, it shows an error
    message box.

    Args:
        None
    Returns:
        None
    '''

    try:
        num1 = float(entry_operand1.get())
        num2 = float(entry_operand2.get())
        result = num1 - num2
        tk.messagebox.showinfo("Result", f"The result is: {result}")
    except ValueError:
        tk.messagebox.showerror("Input Error", "Please enter valid numbers.")

def multiply_numbers():
    '''
    Function to multiply two numbers entered in the entry fields.

    It retrieves the numbers from the entry fields and if valid, performs
    the multiplication operation. If invalid input is detected, it shows an error
    message box.
    Args:
        None
    Returns:
        None
    '''

    try:
        num1 = float(entry_operand1.get())
        num2 = float(entry_operand2.get())
        result = num1 * num2
        tk.messagebox.showinfo("Result", f"The result is: {result}")
    except ValueError:
        tk.messagebox.showerror("Input Error", "Please enter valid numbers.")

def divide_numbers():
    '''
    Function to divide two numbers entered in the entry fields.

    It retrieves the numbers from the entry fields and if valid, performs
    the division operation. If invalid input is detected, it shows an error
    message box. It also checks for division by zero and raises an error if
    attempted.
    Args:
        None
    Returns:
        None
    '''

    try:
        num1 = float(entry_operand1.get())
        num2 = float(entry_operand2.get())
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        result = num1 / num2
        tk.messagebox.showinfo("Result", f"The result is: {result}")
    except ValueError:
        tk.messagebox.showerror("Input Error", "Please enter valid numbers.")
    except ZeroDivisionError as e:
        tk.messagebox.showerror("Math Error", str(e))

# Create the main window for the calculator
window_calulator = tk.Tk()

if platform.system() == "Darwin":
    # OSX Entry boxes are larger, so windows width needs to be larger
    window_calulator.geometry("515x200")
    window_calulator.resizable(0,0)
else:
    # For Windows and Linux, set a smaller window size
    window_calulator.geometry("345x200")
    window_calulator.resizable(0,0)
# Set a custom title for the window
window_calulator.title("Basic Calulator")
# Set the background color
window_calulator.configure(bg="#D8D7D7") # Set background color to light grey

# Set the default value for the current operator
current_operator = tk.StringVar()
current_operator.set("add_nums")  # Default operator

# Create IntVar for the entry fields to hold the operands
entry_operand1 = tk.StringVar()
entry_operand2 = tk.StringVar()
# Initialize the entry fields with empty strings
entry_operand1.set("")
entry_operand2.set("")

# test
# print(current_operator.get())

# Create radio buttons for the four basic arithmetic operations

button_plus = tk.Radiobutton(window_calulator, text="+", variable=current_operator, value="add_nums")
button_minus = tk.Radiobutton(window_calulator, text="-", variable=current_operator, value="subtract_nums")
button_multiply = tk.Radiobutton(window_calulator, text="*", variable=current_operator, value="multiply_nums")
button_divide = tk.Radiobutton(window_calulator, text="/", variable=current_operator, value="divide_nums")

# Place the operand radio buttons in the grid
button_plus.grid(row=0, column=1, padx=5, pady=(10,5))
button_minus.grid(row=1, column=1, padx=5, pady=5)
button_multiply.grid(row=2, column=1, padx=5, pady=5)
button_divide.grid(row=3, column=1, padx=5, pady=5)

# Create Evaluate button to perform the selected operation
button_evaluate = tk.Button(window_calulator,
                            text="Evaluate",
                            command=operate)
# Place the Evaluate button in the grid
button_evaluate.grid(row=4, column=1, padx=5, pady=(5,10))

# Create entry fields for the two operands

entry_operand1 = tk.Entry(window_calulator, textvariable=entry_operand1)
entry_operand2 = tk.Entry(window_calulator, textvariable=entry_operand2)

# Place the entry fields in the grid
entry_operand1.grid(row=2, column=0, padx=(10,5), pady=5)
entry_operand2.grid(row=2, column=3, padx=5, pady=5)

# Run the application
window_calulator.mainloop()
