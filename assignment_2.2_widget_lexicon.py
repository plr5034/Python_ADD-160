'''
Assignment 2.2 A small lexicon of widgets - Part 2
Author: Paul Ring
github link: https://github.com/plr5034/Python_ADD-160/blob/main/assignment_2.2_widget_lexicon.py

Create an interface demonstrating the use of all the widgets covered in this
lesson:
    - Label
    - Message
    - Frame
    - LabelFrame
    - Entry
    
Additionally, include a Button that retrieves the text from the Entry widget
and displays it in a Label using a textvariable.
'''

# Importing necessary modules
import tkinter as tk

    # Function to quit the application
def on_quit():
    '''
    Quit the application.

    Args:
        None
    Returns:
        None
    '''
    window_widget_demo.destroy()

# Create the main window
window_widget_demo = tk.Tk()
window_widget_demo.title("Widget Demo")

# 1) combining the label, frame and message widgets into one area

# Create a static text label for the frame and message that follows:
demo_label = tk.Label(window_widget_demo, text="Demo Label, Frame and Message...")
demo_label.pack(pady=10, padx=10)

# Create a frame to hold the message widget
frame_message = tk.Frame(window_widget_demo, bd=2, relief=tk.SUNKEN)
frame_message.pack(padx=10, pady=10)

# Create a message widget inside the frame
lincoln_message = tk.Message(frame_message,
                     text="Four score and seven years ago our fathers\n"
                     "brought forth on this continent, a new nation,\n"
                     "conceived in Liberty, and dedicated to the\n"
                     "proposition that all men are created equal..", width=300)
lincoln_message.pack(padx=10, pady=10)

# 2) Create a labelframe to hold the entry widget and button and dynamic
# text label
labelframe_entry = tk.LabelFrame(window_widget_demo, text="Entry and Button", padx=10, pady=10)
labelframe_entry.pack(padx=10, pady=10)

# Create an entry widget for user input
entry_demo_text = tk.Entry(labelframe_entry)
entry_demo_text.pack(pady=10, padx=10)

# Create a button to fetch the entry data and display it in a label
def show_entry_data():
    '''
    Display the text from the entry widget in a message box.
    
    Args:
        None
    Returns:
        None
    '''
    entry_data = entry_demo_text.get()
    dynamic_text.set(entry_data)


# Create a button to fetch the entry data and display it in a label
button = tk.Button(labelframe_entry,
                   text="Show Entry Data",
                   command=show_entry_data)
button.pack()

dynamic_text = tk.StringVar()

# Create a label to display the dynamic text
dynamic_label = tk.Label(labelframe_entry, textvariable=dynamic_text)
dynamic_label.pack(pady=10)

# Bonus button :)  This button is outside the frames and  will quit the
# application
quit_button = tk.Button(window_widget_demo,
                        text="Quit",
                        command=on_quit)
quit_button.pack(pady=(10,20))

# Run the application
window_widget_demo.mainloop()
