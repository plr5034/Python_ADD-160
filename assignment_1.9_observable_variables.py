'''
Assignment 1.9 Using Observable Variables in Tkinter
Author: Paul Ring
github link: https://github.com/plr5034/Python_ADD-160/blob/main/assignment_observable_variables.py

Understand and use observable variables in Tkinter to manage dynamic data in
their Python applications. They will also learn how to create and use entry
widgets.

1) Initializing the Main Window
Before declaring observable variables, you must initialize the main window
of your Tkinter application using the tk.Tk() method.

2)  Declaring Observable Variables
Next, let's declare observable variables for the user's name and age,
and a message variable to hold the dynamic message.

3) Creating Entry Widgets
To get input from the user, we need to create entry widgets for the name and
age. We'll also add labels to indicate what each entry is for.

4) Adding Observers
Now we will add observers to the name and age variables. These observers will
call a function to update the message whenever the user changes their input.

5) Displaying the Dynamic Message
Finally, we need to add a label to display the dynamic message that gets 
updated based on the user's input.

'''

import tkinter as tk

# Initialize the main window - observable variable demo window
ov_demo_window = tk.Tk()
ov_demo_window.title("Greeting App")

# Declare observable variables
name_var = tk.StringVar()
age_var = tk.StringVar()
message_var = tk.StringVar()


# Create the user interface
tk.Label(ov_demo_window, text="Name:").grid(row=0, column=0)
tk.Entry(ov_demo_window, textvariable=name_var).grid(row=0, column=1)

tk.Label(ov_demo_window, text="Age:").grid(row=1, column=0)
tk.Entry(ov_demo_window, textvariable=age_var).grid(row=1, column=1)


# Define the function to update the message
def update_message(*args):
    name = name_var.get()
    age = age_var.get()
    
    if name and age:
        message_var.set(f"Hello, {name}! You are {age} years old.")
    else:
        message_var.set("")

# Add observers
name_var.trace("w", update_message)
age_var.trace("w", update_message)

# Create the label to display the message
tk.Label(ov_demo_window, textvariable=message_var).grid(row=2, columnspan=2)

# Start the Tkinter event loop
ov_demo_window.mainloop()