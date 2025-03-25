'''
Assignment 2.5 Working with the Canvas
Author: Paul Ring
github link: https://github.com/plr5034/Python_ADD-160/blob/main/assignment_2.5_canvas.py

Create a canvas, set a background color, and draw a simple image like a 
Christmas tree with ornaments. Add text to the canvas as well.

1) Create a Tkinter canvas with a specified width, height, and background color.
2) Draw a Christmas tree (3 triangles with a rectangle for the trunk).
3) Add circles to represent ornaments on the tree.
4) Add a text message, such as "Happy Holidays!"
'''

# Import the necessary libraries
import tkinter as tk

# Initialize the main window using Tkinter
window_canvas = tk.Tk()

# Set a custom title and icon for the window
window_canvas.title("Christmas Tree Canvas")

# Create a canvas with specified dimensions and background color
canvas = tk.Canvas(window_canvas, width=350, height=450, bg='gray', borderwidth=2)
canvas.pack()

# Draw the tree (triangle)
canvas.create_polygon(180, 50, 230, 150, 130, 150, outline='green', fill='green', width=2)
canvas.create_polygon(180, 100, 255, 225, 105, 225, outline='green', fill='green', width=2)
canvas.create_polygon(180, 150, 280, 300, 80, 300, outline='green', fill='green', width=2)

# Draw the trunk (rectangle)
canvas.create_rectangle(155, 300, 205, 350, outline='brown', fill='brown', width=2)

# Draw ornaments (circles of various colors and locations on tree)
canvas.create_oval(180, 75, 190, 85, outline='red', fill='red', width=2)
canvas.create_oval(160, 100, 170, 110, outline='blue', fill='blue', width=2)
canvas.create_oval(200, 120, 210, 130, outline='yellow', fill='yellow', width=2)
canvas.create_oval(170, 130, 180, 140, outline='red', fill='red', width=2)
canvas.create_oval(190, 160, 200, 170, outline='blue', fill='blue', width=2)
canvas.create_oval(160, 180, 170, 190, outline='yellow', fill='yellow', width=2)
canvas.create_oval(215, 195, 225, 185, outline='red', fill='red', width=2)
canvas.create_oval(130, 200, 140, 210, outline='blue', fill='blue', width=2)
canvas.create_oval(205, 220, 215, 230, outline='yellow', fill='yellow', width=2)
canvas.create_oval(155, 230, 165, 240, outline='red', fill='red', width=2)
canvas.create_oval(225, 250, 235, 260, outline='blue', fill='blue', width=2)
canvas.create_oval(125, 270, 135, 280, outline='yellow', fill='yellow', width=2)
canvas.create_oval(210, 280, 220, 290, outline='red', fill='red', width=2)
canvas.create_oval(180, 260, 190, 270, outline='blue', fill='blue', width=2)

# Add text
canvas.create_text(180, 380, text="Merry Christmas,", font=('Papyrus', 20), fill='black')
canvas.create_text(180, 410, text="and Happy New Year!", font=('Papyrus', 20), fill='black')

# Run the application
window_canvas.mainloop()
