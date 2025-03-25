'''
Assignment 2.4 Shaping the main window and conversing with the user
Author: Paul Ring
github link: https://github.com/plr5034/Python_ADD-160/blob/main/assignment_2.4_conversing.py

Combine all the features you've learned so far about Tkinter into a single 
application. Create:
    * a customized main window
    * display various message boxes
    * use dialog functions to interact with the user.

Follow the high-level directions below to complete the assignment.

1) Create the Main Window:
    * Initialize the main window using Tkinter.
    * Set a custom title and icon for the window.
    * Specify the window size and set minimum and maximum size limits.
    * Implement a close window button that asks for confirmation before closing the window.

2) Display Message Boxes:
    * Show an error message box with a custom title and message.`
    * Show a warning message box with a custom title and message.
    * Show an informational message box with a custom title and message.

3) Use Dialog Functions:
    * Implement the askyesno function to ask the user a yes/no question and handle the response.
    * Implement the askokcancel function to ask the user an ok/cancel question and handle the response.
    * Implement the askretrycancel function to ask the user a retry/cancel question and handle the response.

4) Combine Features:
    * Ensure all the above features are integrated into a single Tkinter application.
    * Test the application to ensure it works as expected.
'''

# Import the necessary libraries
import tkinter as tk
from tkinter import messagebox
import platform # needed to set icon path

# Define a function to handle window close
def on_closing():
    '''
    Method to handle the window close event.

    Ask the user for confirmation before closing the window.

    Args:
        None
    Returns:
        None
    '''
    if messagebox.askokcancel("Quit", "Do you really want to quit?"):
        dialog_demo_window.destroy()

def show_error_message():
    '''
    Method to handle the Show Error selection.

    Will show an error message box with a custom title and message.
    Will implement the askyesno function to ask the user a yes/no
    question and handle the response.

    Args:
        None
    Returns:
        None
    '''
    if not messagebox.askyesno("Oops!", "There was an\nUndefined Application Error!\n\nContinue?"):
        dialog_demo_window.destroy()

def show_warn_message():
    '''
    Method to handle the Show Warning selection.

    Will show a warning message box with a custom title and message.
    Will implement the askokcancel function to ask the user an ok/cancel
    question and handle the response.

    Args:
        None
    Returns:
        None
    '''
    if not messagebox.askokcancel("Oh no!", "If you continue, all previous data will be lost!\n\nContinue?"):
        dialog_demo_window.destroy()

def show_info_message():
    '''
    Method to handle the Show Information selection.

    Will show an information message box with a custom title and message.
    Will implement the askretrycancel function to ask the user a retry/cancel
    question and handle the response.

    Args:
        None
    Returns:
        None
    '''
    if not messagebox.askretrycancel("Hey, fyi...", "There was a momentary lapse of sanity...\nWould you like to retry or cancel?"):
        dialog_demo_window.destroy()

# Initialize the main window using Tkinter
dialog_demo_window = tk.Tk()

# Set a custom title and icon for the window
dialog_demo_window.title("Dialog Demo Window")

# Set the window icon (icon must be a .ico file)
my_computer_os = platform.system()
if my_computer_os=="Darwin":
    # MacOS call does not work :(
    dialog_demo_window.iconbitmap('/Users/Shared/icon.png')
if my_computer_os=="Linux":
    dialog_demo_window.iconbitmap('/home/shared/icon.ico')
elif my_computer_os=="Windows":
    dialog_demo_window.iconbitmap("c:\\Users\\Public\\icon.ico")

# Specify the window size and set minimum and maximum size limits.
dialog_demo_window.geometry("360x300")  # Width x Height
dialog_demo_window.minsize(260, 225)  # Minimum width and height
dialog_demo_window.maxsize(460, 375)  # Maximum width and height

# Create a label frame for the message demo buttons
labelframe_message = tk.LabelFrame(dialog_demo_window,
                                   text="Dialog Demonstration Buttons",
                                   padx=10, pady=10)
labelframe_message.pack(padx=10, pady=10)

# Buttons for displaying message boxes

button_error = tk.Button(labelframe_message,
                   text="Error Message",
                   command=show_error_message)
button_error.pack(pady=5)

button_warning = tk.Button(labelframe_message,
                   text="Warning Message",
                   command=show_warn_message)
button_warning.pack(pady=5)

button_info = tk.Button(labelframe_message,
                   text="Info Message",
                   command=show_info_message)
button_info.pack(pady=5)

# Bind the close window protocol to valid the user wants to 
# close the window and quit the applicaiton
dialog_demo_window.protocol("WM_DELETE_WINDOW", on_closing)

# Implement a close window button that asks for confirmation before closing
# the window

quit_button = tk.Button(dialog_demo_window,
                        text="Quit",
                        command=on_closing)
quit_button.pack(pady=5)

# Run the application
dialog_demo_window.mainloop()
