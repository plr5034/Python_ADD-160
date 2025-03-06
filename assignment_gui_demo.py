'''
Assignment 1.4 Coloring your widgets
Name: Paul Ring
github link: https://github.com/plr5034/Python_ADD-160/blob/main/assignment_gui_demo.py

Objective: Deomonstrate adding color to various widgets

Change the colors of various widgets in a Tkinter GUI application. 
Specifically:

    * Change the color of a button in both its raised and pressed 
    states using color names.
    * Change the color of a button using RGB values.
    * Create a complete form with RGB-colored backgrounds for all 
    components, including a close button.

This application will use the grid geometry manager to layout the
widgets.

* Use descriptive names for your functions and variables to make your code
    easier to understand.
Experiment with different colors to create a visually appealing application.
Ensure your buttons and labels are easily distinguishable and appropriately
    spaced.

NOTE: coloring backgrounds do not work on Mac OS, but do on Win/Linux
https://github.com/python/cpython/issues/88409

Can fix by installing tkmacosx and importing appropriate widgets
but need to then test platform and use logic to import correct widgets
and code
'''

#
#   tkinter binding events
#   https://python-course.eu/tkinter/events-and-binds-in-tkinter.php
#   https://dafarry.github.io/tkinterbook/tkinter-events-and-bindings.htm
#   https://stackoverflow.com/questions/32289175/list-of-all-tkinter-events
#

# 2. Import the tkinter module
import tkinter as tk

# 4. Define Color Change Funtions
# Create two functions for each button. 
# One function should change the button's color when pressed, 
# and the other should reset the color when the button is released. 

def on_top_left_press(event):
    ''' 
    Function to change top left button color to black with white text
    when pressed
    '''
    event.widget.config(activebackground='black', activeforeground='white')
    print("Button pressed")

def on_top_left_release(event):
    '''
    Function to reset top left button color to white with black text
    when released
    '''
    event.widget.config(bg='white', fg='black')
    print("Button released")

def on_center_press(event):
    ''' 
    Function to change center button color to Yellow with Forest Green
    text when pressed
    '''
    event.widget.config(activebackground='#FFF000', activeforeground='#045F04')  

def on_center_release(event):
    '''
    Function to reset center button color to Forest Green with Yellow
    text released
    '''
    event.widget.config(bg='#045F04', fg='#FFF000')  

def on_bottom_right_button_press(event):
    ''' 
    Function to change bottom right button color to confederate blue with Rose
    text when pressed
    '''
    event.widget.config(activebackground='#042C5F', activeforeground='#E44C86')  

# Function to reset button_threes color when released
# Rose background, confederate blue text
def on_bottom_right_button_release(event):
    '''
    Function to reset bottom right button color to Rose with confederate blue
    text released
    '''
    event.widget.config(bg='#E44C86', fg='#042C5F')  

# 3. Create the main application window

main_app_window = tk.Tk()
main_app_window.title("Widget Coloring Demo ")

# 5. Create Buttons
# Create three buttons, each with different colors for their raised and
#   pressed states
# Assign the appropriate functions to the on_button_(number)_press and 
#   on_button_(number)_release events of each button.

# 6. Create labels
# Create three labels to accompany the buttons. 
# These labels can describe the buttons or provide additional information.

# White background, black text
top_left_button = tk.Button(main_app_window, text="Top Left", bg='white', fg='black')
top_left_button.bind("<Button-1>", on_top_left_press)  #on_top_left_button_press)
top_left_button.bind("<ButtonRelease-1>", on_top_left_release)#on_top_left_button_release)
# Forest Green background, Yellow text
center_button = tk.Button(main_app_window, text="Center", bg='#045F04', fg='#FFF000')
center_button.bind("<ButtonPress-1>", on_center_press)
center_button.bind("<ButtonRelease-1>", on_center_release)
# Rose background, confederate blue text
bottom_right_button = tk.Button(main_app_window, text="Bottom Right", bg='#E44C86', fg='#042C5F')
bottom_right_button.bind("<ButtonPress-1>", on_bottom_right_button_press)
bottom_right_button.bind("<ButtonRelease-1>", on_bottom_right_button_release)
#button to close the application
close_button = tk.Button(main_app_window, text="Close", bg='white'
                         , fg='black', command=main_app_window.quit)

# 7. Use the Grid Layout
# Use the grid layout to organize the buttons and labels 
# within the main window. 
# Ensure that each component is properly aligned and spaced.
# Since no specifics provided, buttons are placed in a 3x3 grid
# with each button in different rows and columns

top_left_button.grid(row=0, column=0, padx=5, pady=5)
center_button.grid(row=1, column=1, padx=5, pady=5)
bottom_right_button.grid(row=2, column=2, padx=5, pady=5)
close_button.grid(row=3, column=1, padx=5, pady=5)

# 8. Run the Application:
# Start the Tkinter event loop to run the application.
#  This will display the window and allow users to interact with the buttons.
main_app_window.mainloop()