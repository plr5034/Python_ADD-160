'''
Homework Week 7 - joke_app.py
Name:Paul Ring 
github link: https://github.com/plr5034/Python_ADD-160/blob/main/joke_app.py

Simple demonstration of GUI programming

This application will be a denonstrate some very basic GUI building
techniques with common widgets including:

Labels: Used to display text or images.
Buttons: Used to perform an action when clicked.
Entry Fields: Used to input text.
Checkbuttons and Radiobuttons: Used for selecting options.

Also introduces event driven programming

'''
import tkinter as tk
from tkinter import messagebox

# Create the main window with title and set size
root = tk.Tk()
root.title("Joke")
root.geometry("300x150")

# Add a label with the joke setup
joke_label = tk.Label(root, text="Why don't scientists trust atoms?")
joke_label.pack(pady=20)

def show_punchline():
    '''
    Function to show the punchline in dialog/message box
    
    Args: 
        None
    Returns:
        None
    '''
    messagebox.showinfo("Punchline", "Because they make up everything!")
    root.destroy()

# Add a button to show the punchline dialog/message box
punchline_button = tk.Button(root, text="Show Punchline", command=show_punchline)
punchline_button.pack(pady=10)

# Run the application
root.mainloop()
