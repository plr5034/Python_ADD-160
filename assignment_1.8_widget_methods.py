'''
Assignment 1.8 Tkinter Widget Methods
Author: Paul Ring
github link: https://github.com/plr5034/Python_ADD-160/blob/main/assignment_widget_methods.py

Create a Tkinter application by modifying the background color change
function, adding a new button to change the window size, and creating another
button to change the text of the "Goodbye!" button.

1) Modify Background Color and Time Interval:
    * Change the function that modifies the background color to use a different
      color of your choice.
    * Adjust the time interval for the background color change.
2) Add Button to Change Window Size:
    * Create an additional button in the Tkinter window.
    * Program this button to change the size of the window when clicked.
3) Create a Button to Change the Text of "Goodbye!" Button:
    * Add a new button that, when clicked, changes the text of the
      "Goodbye!" button.
'''

# Importing necessary modules
import tkinter as tk
from tkinter import ttk # need this for combobox

# Global variables
is_tan = True       # Default background color is tan
is_portrait = True  # Default window size is portrait
swap_period = 5000  # Default period for background color change

# Define a function to change the background color of the window
# This function will be called periodically to swap the background color
# based on the selected time interval from the ComboBox

def background_swap():
    '''
    Change the background color of the window.

    Args:
        None
    Returns:
        None
    '''
    global is_tan
    my_period = selected_increment.get()    # Get the selected time interval
    my_swap_period = int(my_period) * 1000  # Convert seconds to milliseconds
    print("background_swap:", my_swap_period)
    method_window.after(my_swap_period, background_swap)
    if is_tan:
        color = 'lightgreen'
    else:
        color = 'tan'
    is_tan = not is_tan
    method_window.config(bg=color)


def toggle_window_size():
    '''
    Toggle the size of the window between portrait and landscape.

    Args:
        None
    Returns:
        None
    '''
    global is_portrait
    if is_portrait:
        win_dimension = '550x400'
    else:
        win_dimension = '400x550'
    is_portrait = not is_portrait
    print("Changing window size")
    method_window.geometry(win_dimension)

# Define a function to toggle button text using cget() and config()
def toggle_beatle_button_text():
    '''
    Toggle the text of the "Goodbye!" button, from "Goodbye" to "Hello" and vice versa.

    Args:
        None
    Returns:
        None
    '''
    current_text = beatle_button.cget("text")
    if current_text == "Hello":
        beatle_button.config(text="Goodbye")
    else:
        beatle_button.config(text="Hello")

    # Function to quit the application
def on_quit():
    '''
    Quit the application.

    Args:
        None
    Returns:
        None
    '''
    method_window.destroy()

# 1) Create the Main Application Window:
#   a) Initialize the Tkinter window.
#   b) Set the title of the window.
#   c) Set the default size of the window.
#   d) Set the initial background color to tan.

method_window = tk.Tk()
method_window.title("Widget Method Demo")
method_window.geometry("400x550")  # Set the window size
method_window.configure(bg="tan")  # Set the initial background color to tan

# 2) Create a ComboBox to change the interval of the background color change
#   a) Create a label for the ComboBox.
#   b) Create a ComboBox with a list of time intervals.
#   c) Set the default time interval to 1 second.
#   d) Create a function to change the time interval based on the selected value.

combo_label = ttk.Label(text="Please select the background toggle period (secs):")
combo_label.pack(padx=10, pady=(20,10))

time_increments = ["6",
                   "8",
                   "10",
                   "12",
                   "14",
                   "16",
                   "18",
                   "20"]

selected_increment = tk.StringVar()
selected_increment.set(time_increments[0])

increment_dropdown = tk.OptionMenu(method_window,
                                   selected_increment,
                                   *time_increments)
increment_dropdown.pack()
period = selected_increment.get()
method_window.after(swap_period, background_swap)

# 3) Create a Button to Toggle the Window Size:
#   a) Create a button that says "Toggle Window Size".
#   b) Program this button to change the size of the window when clicked.
#   c) Set focus on the window size button.
#   d) Create a function to toggle the size of the window.

size_button_label = tk.Label(text="Click to Toggle the window size.")
size_button_label.pack(pady=(40,0))
size_button = tk.Button(method_window,
                        text="Toggle Window Size",
                        command=toggle_window_size)
size_button.pack(pady=20)
size_button.focus_set() # Set focus on the window size button

# 4) Create a Button to Change the Text of the "Goodbye!" Button:
#   a) Create a button that says "Googbye!".
#   b) Program this button to change the text of the "Goodbye!" button when clicked to Hello!
#   c) Create a function to change the text of the "Goodbye!" button.

beatle_button_label = tk.Label(text="Click to change the text of the 'Goodbye!' button.")
beatle_button_label.pack(pady=10)
beatle_button = tk.Button(method_window,
                          text="Goodbye",
                          command=toggle_beatle_button_text)
beatle_button.pack(pady=(10,20))

# Bonus button :)  This button will quit the application
quit_button = tk.Button(method_window,
                        text="Quit",
                        command=on_quit)
quit_button.pack(pady=(20,10))

# Run the application
method_window.mainloop()
