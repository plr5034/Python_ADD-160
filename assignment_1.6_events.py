'''
Assignment 1.6 GUI Application with Multiple Buttons
Name: Paul Ring
github link: https://github.com/plr5034/Python_ADD-160/blob/main/assignment_events.py

Create a Python GUI application with multiple buttons that perform different
actions, such as changing the background color of the window, displaying
lines of a song or poem one at a time, and one other action of your choice.

1) Create the Main Application Window:
2) Add Buttons for Different Actions:
3) Implement the Background Color Change:
4) Implement the Display of Song or Poem Lines:
5) Choose and Implement an Additional Action:
    a) Display Current Date and Time ** Added this one
    b) Count Button Clicks
    c) Toggle Text 

'''

# Importing necessary modules
import tkinter as tk
from tkinter import messagebox
from datetime import datetime # need for display_date function

# Function to be called when the "Now" button is clicked
def display_date():
    '''
    Display the current date and time in a message box.

    Args:
        None
    Returns:
        None
    '''
    # get date and put in variable
    date_now = datetime.now()
    date_time_now = date_now.strftime("%m/%d/%Y %H:%M:%S")
    # Show message box with the current date
    messagebox.showinfo("Date and Time", date_time_now)

# 1) Create the Main Application Window:
#   a) Initialize the Tkinter window.
#   b) Set the title of the window.
#   c) Set the default size of the window.
#   Create a frame for the three buttons to reside in

event_window = tk.Tk()
event_window.title("Three Button Demo")
event_window.geometry("350x560")

# Set the default background color of the window
event_window.configure(background='tan')

# Variable to keep track of the current line number
lyric_num = 0

# Function to quit the application
def on_quit():
    '''
    Quit the application.

    Args:
        None
    Returns:
        None
    '''
    event_window.destroy()

def change_bg_color(event):
    '''
    Toggle the background color of the window between three colors.

    The function changes the background color of the window between 
    tan (default), light blue and light green.
    '''
    # List of background colors to toggle between
    bg_colors = ['tan', 'light blue', 'light green']
    current_color = event_window.cget('background') # get the current color
    # Find the index of the current color in the list
    color_index = bg_colors.index(current_color)
    next_color_index = (color_index + 1) % len(bg_colors) # wrap around
#    print(f"Current color: {current_color}")
    next_color = bg_colors[next_color_index]
#    print(f"Next color: {next_color}")
    event_window.configure(background=next_color) # set the next color

def display_lines():
    '''
    Display lines of a song or poem one at a time.

    The function displays lines of a song or poem one at a time when the
    button is clicked.  It should cycle through the lines until the end
    of the song or poem.

    Args:
        None
    Returns:
        None
    '''
    # Exit Music (For A Film) by Radiohead
    song_lines = [
        "Wake from your sleep",
        "The drying of your tears",
        "Today we escape, we escape",
        "Pack and get dressed",
        "Before your father hears us",
        "Before all hell breaks loose",
        "Breathe, keep breathing",
        "Don't lose your nerve",
        "Breathe, keep breathing",
        "I can't do this alone",
        "Sing us a song",
        "A song to keep us warm",
        "There's such a chill",
        "Such a chill",
        "And you can laugh a spineless laugh",
        "We hope your rules and wisdom choke you",
        "Now we are one in everlasting peace",
        "We hope that you choke, that you choke"]

    # Display the next line from the song
    # If the end of the song is reached, start over
    global lyric_num
    if lyric_num < len(song_lines):
        line_display_label.config(text=song_lines[lyric_num])
        lyric_num += 1
    else:
        lyric_num = 0
        line_display_label.config(text=song_lines[lyric_num])

# 2) Add Buttons for Different Actions: 
#   * Create a button that changes the background color of the window.
#   * Create a button that displays lines of a song or poem one at a time.
#   * Choose one additional action (suggestions provided below) and create
#   a button for it.
#


# 3) Create a button that changes the background color of the window:
#   * Define a function that changes the window's background color to
#   another color, it should toggle between two or more colors.
#   * Bind this function to the button.

# Create a frame to hold the background color label and toggle button
# NOTE: once add widgets to frame, a default width and height
# don't seem to work
color_toggle_button_frame = tk.LabelFrame(event_window,
                            text="Background Changer",
                            borderwidth=3,
                            relief='groove',
                            padx=15,
                            pady=15)
color_toggle_button_frame.pack(padx=10, pady=(20,10)) # more padding on top

color_toggle_button_label = tk.Label(color_toggle_button_frame, 
                                     text="Click the \"Toggle It!\" button to \n change the window background color")
color_toggle_button_label.pack()

color_toggle_button = tk.Button(color_toggle_button_frame, text="Toggle It!")
color_toggle_button.bind("<Button-1>", change_bg_color)
color_toggle_button.pack(pady=10)

# 4) Create a button that displays lines of a song or poem one at a time:
#   * Define a list containing lines of a song or poem.
#   * Create a function that displays the next line from the list each time
#   the button is clicked.
#   * Bind this function to the button.

# Create a frame to hold the display song button and line result

display_line_button_frame = tk.LabelFrame(event_window,
                            text="Song Lines",
                            borderwidth=3,
                            relief='groove',
                            padx=15,
                            pady=15)
display_line_button_frame.pack(padx=10, pady=(10))

display_line_button_label = tk.Label(display_line_button_frame, 
                                     text="Click the \"Next Line\" button to show\n the next line of \"Exit Music (For A Film)\"")   
display_line_button_label.pack()

display_line_button = tk.Button(display_line_button_frame, text="Next Line", command=display_lines)
display_line_button.pack(pady=10)

# Create a label to display the current line of the song
line_display_label = tk.Label(display_line_button_frame, text="")
line_display_label.pack()

# 5) Choose one additional action and create a button for it:
#   * Display the current date and time in a message box.   The function will
#   retrieve and display the current date and time and display it in a
#   message box when you click the button.

# Create a frame to hold the date and time button and label

date_time_button_frame = tk.LabelFrame(event_window,
                            text="Date and Time",
                            borderwidth=3,
                            relief='groove',
                            padx=15,
                            pady=15)
date_time_button_frame.pack(padx=10, pady=(10))

date_time_button_label = tk.Label(date_time_button_frame, 
                                     text="Click the \"Now!\" button\nto show the current date and time")
date_time_button_label.pack()

date_time_button = tk.Button(date_time_button_frame, text="Now!", command=display_date)
date_time_button.pack(pady=10)

# Bonus button :)  This button will quit the application

quit_button = tk.Button(event_window, text="Quit", command=on_quit)
quit_button.pack(pady=10)

# Run the application
event_window.mainloop()
