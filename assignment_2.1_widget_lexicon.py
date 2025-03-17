'''
Assignment 2.1 A small lexicon of widgets - Part 1
Author: Paul Ring
github link: https://github.com/plr5034/Python_ADD-160/blob/main/assignment_2.1_widget_lexicon.py

Modify a Tkinter application that currently:

    * Creates a window using Tkinter
    * Uses frames for organizing widgets
    * Implements data entry fields, labels, checkboxes, and buttons
        - orginianl app uses the following fields:
            - Name
            - Email
            - Phone
            - Phone Type
    *  Uses a grid layout for arranging widgets
    *  Displays information using a message box
    *  Creates a button to quit the application

1) Modify the application to:
    - Add an additional field for "Address".  Assume that includes:
        - Street
        - City
        - State
        - Zipcode
'''

# Importing necessary modules
import tkinter as tk
from tkinter import messagebox

# Create the main window
data_entry_window = tk.Tk()
data_entry_window.title("Contact Information Form")

# Create frames:
#   1) Frame for data entry fields
#   2) Frame for buttons

frame_data_entry = tk.Frame(data_entry_window)
frame_buttons = tk.Frame(data_entry_window)

# Place the frames in the window using grid layout
frame_data_entry.grid(row=0, column=0, padx=10, pady=10)
frame_buttons.grid(row=1, column=0, padx=10, pady=10)

# Name entry and placement
label_name = tk.Label(frame_data_entry, text="Name:")
entry_name = tk.Entry(frame_data_entry)

label_name.grid(row=0, column=0, sticky='w')
entry_name.grid(row=0, column=1)

# Contact Address entry and placement
label_street_address = tk.Label(frame_data_entry, text="Street:")
entry_street_address = tk.Entry(frame_data_entry)

label_street_address.grid(row=1, column=0, sticky='w')
entry_street_address.grid(row=1, column=1)

# Contact City entry and placement
label_city = tk.Label(frame_data_entry, text="City:")
entry_city = tk.Entry(frame_data_entry)

label_city.grid(row=2, column=0, sticky='w')
entry_city.grid(row=2, column=1)

# Contact State entry and placement
# TODO: Change this to an option menu with the 50 states
label_state = tk.Label(frame_data_entry, text="State:")
entry_state = tk.Entry(frame_data_entry)

label_state.grid(row=3, column=0, sticky='w')
entry_state.grid(row=3, column=1)

# Contact Zipcode entry and placement
# TODO: Add a validation function to check for 5 digit zip code
label_zipcode = tk.Label(frame_data_entry, text="Zipcode:")
entry_zipcode = tk.Entry(frame_data_entry)

label_zipcode.grid(row=4, column=0, sticky='w')
entry_zipcode.grid(row=4, column=1)

# Contact Email entry and placement
label_email = tk.Label(frame_data_entry, text="Email:")
entry_email = tk.Entry(frame_data_entry)

label_email.grid(row=5, column=0, sticky='w')
entry_email.grid(row=5, column=1)

# Contact Phone entry and placement
label_phone = tk.Label(frame_data_entry, text="Phone:")
entry_phone = tk.Entry(frame_data_entry)

label_phone.grid(row=6, column=0, sticky='w')
entry_phone.grid(row=6, column=1)

# Contact Phone type checkboxes and placement
label_phone_type = tk.Label(frame_data_entry, text="Phone Type:")
phone_type_var = tk.StringVar()
checkbox_home = tk.Checkbutton(frame_data_entry, text="Home", variable=phone_type_var, onvalue='Home')
checkbox_mobile = tk.Checkbutton(frame_data_entry, text="Mobile", variable=phone_type_var, onvalue='Mobile')

label_phone_type.grid(row=7, column=0, sticky='w')
checkbox_home.grid(row=7, column=1, sticky='w')
checkbox_mobile.grid(row=7, column=2, sticky='w')

# Function to display the entered information
def display_info():
    '''
    Display the Contact information entered in the form in a message box.
    
    Args:
        None
    Returns:
        None
    '''
    name = entry_name.get()
    street_address = entry_street_address.get()
    city = entry_city.get()
    state = entry_state.get()
    zipcode = entry_zipcode.get()
    email = entry_email.get()
    phone = entry_phone.get()
    phone_type = phone_type_var.get()
    messagebox.showinfo("Information",
                        f"Name: {name}\nStreet: {street_address}\nCity: {city}\nState: {state}\nZipcode: {zipcode}\nEmail: {email}\nPhone: {phone} ({phone_type})")

# Add buttons to:
#   - Display the entered information in the message box
#   - Quit the application
button_display = tk.Button(frame_buttons, text="Display Information", command=display_info)
button_quit = tk.Button(frame_buttons, text="Quit", command=data_entry_window.destroy)

# Place the buttons in the grid
button_display.grid(row=0, column=0, padx=5, pady=5)
button_quit.grid(row=0, column=1, padx=5, pady=5)

# Run the application
data_entry_window.mainloop()
