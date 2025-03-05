'''
Homework8
Name: Paul Ring
github link: https://github.com/plr5034/Python_ADD-160/blob/main/assignment_form_grid.py

Objective: Create a simple form using Python's Tkinter library and 
the grid Geometry manager.

The form should include labels and entry widgets for the following fields
    - Name
    - Email
    - Password
Ensure that the labels and entry widgets are correctly aligned.
'''

import tkinter as tk

root = tk.Tk()
root.title("Sample...") # added to match example

# Create label and entry widgets for 
# Name, Email, and Password fields
# Looks like exampel width may have been 15,
# but 20 is better for name, maybe even larger
name_lable = tk.Label(root, text="Name:")
name_entry = tk.Entry(root, width=20)

email_label = tk.Label(root, text="Email:")
email_entry = tk.Entry(root, width=20)

password_label = tk.Label(root, text="Password:")
password_entry = tk.Entry(root, width=20)

# Place labels in the grid that is 3 rows, 2 columns
# padx and pady are padding in the x and y directions to
# provide space between the widgets and windows edge
# also add extra padding to the bottom of the password entry
name_lable.grid(row=0, column=0, padx=10, pady=5)
name_entry.grid(row=0, column=1, padx=10, pady=5)
email_label.grid(row=1, column=0, padx=10, pady=5)
email_entry.grid(row=1, column=1, padx=10, pady=5)
password_label.grid(row=2, column=0, padx=10, pady=(5, 10))
password_entry.grid(row=2, column=1, padx=10, pady=(5, 10))

# Start the main loop
root.mainloop()