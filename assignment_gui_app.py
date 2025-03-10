'''
Assignment 1.5 A simple GUI application
Name: Paul Ring
github link: https://github.com/plr5034/Python_ADD-160/blob/main/assignment_gui_app.py

Objective: Demonstrate the use of Tkinter to create a simple GUI application,
specifically:

# Create a basic GUI application using Tkinter.
# Use input fields, labels, and buttons in a Tkinter application.
# Implement radio buttons to determine the type of conversion.
# Perform basic calculations based on user input.
# Update labels dynamically based on user input.

Step-by-Step Guide
1. Setting Up the Basic GUI
2. Adding Input Fields and Labels
3. Adding Radio Buttons for Conversion Type
4. Adding a Calculate Button

NOTE: Broke the radio buttons used for determining the direction of the 
conversion to a separate frame.   Then created a frame for the calculation,
and reordered the widgets to improve the flow.

'''

# Import the Tkinter library
import tkinter as tk

# Create the main window
app_window = tk.Tk()
app_window.title("Weight Converter")

# Create a frame to hold the conversion radio buttons
conversion_frame = tk.LabelFrame(app_window, text="Conversion Direction", padx=15, pady=15)
conversion_frame.pack(padx=10, pady=10)

# Add radio buttons for conversion type
conversion_type = tk.StringVar(value="lb_to_kg")
lb_to_kg_radio = tk.Radiobutton(conversion_frame, text="Pounds to Kilograms",
                                variable=conversion_type, value="lb_to_kg")
lb_to_kg_radio.pack()
kg_to_lb_radio = tk.Radiobutton(conversion_frame, text="Kilograms to Pounds",
                                variable=conversion_type, value="kg_to_lb")
kg_to_lb_radio.pack()

def calculate():
    '''
    Perform the calculation based on the selected conversion type

    The function retrieves the amount from the input field, checks the selected
    conversion type, performs the appropriate calculation, and updates the
    result label with the calculated value.  It also handles invalid input by
    displaying an error message.

    Args:
        None
    Returns:
        None
    
    '''
    try:
        amount = float(amount_entry.get())
        if conversion_type.get() == "lb_to_kg":
            result = amount * 0.453592
            result_label.config(text=f"{amount} lbs is {result:.2f} kg")
        else:
            result = amount / 0.453592
            result_label.config(text=f"{amount} kg is {result:.2f} lbs")
    except ValueError:
        result_label.config(text="Please enter a valid number")

# Create a frame to hold the calculation widgets
calculation_frame = tk.LabelFrame(app_window, text="Calculation", padx=15, pady=15)
calculation_frame.pack(padx=10, pady=10)

# Add a label and input field for the amount
amount_label = tk.Label(calculation_frame, text="Enter the amount:")
amount_label.pack()
amount_entry = tk.Entry(calculation_frame)
amount_entry.pack()

# Add a calculate button
calculate_button = tk.Button(calculation_frame, text="Calculate", command=calculate)
calculate_button.pack()

# Add a label to display the result
result_label = tk.Label(calculation_frame, text="")
result_label.pack()

# Start the main event loop
app_window.mainloop()