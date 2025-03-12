'''
Assignment 1.7 Visiting widget properties
Name: Paul Ring
github link: https://github.com/plr5034/Python_ADD-160/blob/main/custom_widgets.py

Create a Tkinter application with three buttons and three lines of text,
each with different customizations.

1) Create three buttons with different foreground and background colors:
    * Button 1: Choose a foreground and background color of your choice.
    * Button 2: Choose a different foreground and background color.
    * Button 3: Choose another set of varying foreground and background colors.

2) Set the mouse cursor to change when hovering over each button. You can
choose cursors like "hand2", "arrow", etc.

3) Create three lines of text using label widgets. Customize each line with
different fonts, font sizes, and enhancements:
    * Text 1: Choose a font, size, and style (e.g., bold, italic).
    * Text 2: Choose a different font, size, and style.
    * Text 3: Choose another font, size, and style.

4) Optionally, set different foreground and background colors for each line
of text.

5) Align the text differently within their labels using the anchor property
(e.g., west, east, north, south).

6) Use the pack() method to arrange your buttons and labels in the main window.

'''

# Import necessary modules
import tkinter as tk

# Create a main window
property_demo_window = tk.Tk()
property_demo_window.title("Widget Properties Demo")

# 1) Create three buttons with different foreground and background colors:
#    * Button 1: Choose a foreground and background color of your choice. red/blue
#    * Button 2: Choose a different foreground and background color. green/yellow
#    * Button 3: Choose another set of varying foreground and background colors. blue/white
# 2) Set the mouse cursor to change when hovering over each button. hand, watch, spraycan

# Create a frame to hold the three buttons
button_frame = tk.LabelFrame(property_demo_window, text="Buttons", padx=15, pady=15)
button_frame.pack(padx=10, pady=10)

# Create a red button widget that has a custom hand cursor
button1 = tk.Button(button_frame,
                       bg='red',
                       fg='blue', 
                       activebackground='blue', 
                       activeforeground='red',
                       text="Hand",
                       cursor="hand2")
button1.pack(pady=10, padx=10)

# Create a green button widget that has a custom watch cursor
button2 = tk.Button(button_frame,
                       bg='green',
                       fg='yellow', 
                       activebackground='yellow', 
                       activeforeground='green',
                       text="Watch",
                       cursor="watch")
button2.pack(pady=10, padx=10)

# Create a blue button widget that has a custom spraycan cursor
button3 = tk.Button(button_frame,
                       bg='blue',
                       fg='white', 
                       activebackground='white', 
                       activeforeground='blue',
                       text="Spraycan",
                       cursor="spraycan")
button3.pack(pady=10, padx=10)

# 3) Create three lines of text using label widgets. Customize each line with
#    different fonts, font sizes, and enhancements:
#    * Text 1: Choose a font, size, and style (e.g., bold, italic).
#    * Text 2: Choose a different font, size, and style.
#    * Text 3: Choose another font, size, and style.
# 4) Optionally, set different foreground and background colors for each line
#    of text.
# 5) Align the text differently within their labels using the anchor property
#    (e.g., west, east, north, south).

# Create a frame to hold the three lines of text
text_frame = tk.LabelFrame(property_demo_window,
                            text="Text Styles",
                            width=500,
                            height=150,
                            padx=15,
                            pady=15)
text_frame.pack(padx=10, pady=10)
#Stop the frame from propagating the widget to be shrink or fit
text_frame.pack_propagate(False)

# Create text (label) widgets with different fonts
text1 = tk.Label(text_frame, 
                  text="Do not go gentle into that good night,",
                  font=("Courier New", 10, "bold"),
                  cursor="hand2",
                  anchor="nw")
text2 = tk.Label(text_frame,
                  text="Old age should burn and rage at close of day;",
                  font=("Arial", 14, "italic"),
                  bg="lightyellow",
                  fg="orange",
                  cursor="star",
                  anchor="ne")
text3 = tk.Label(text_frame,
                  text="Rage, rage against the dying of the light.",
                  font=("Times New Roman",18, "underline"),
                  bg="yellow",
                  fg="red",
                  cursor="pirate",
                  anchor="center")

# Pack the labels
text1.pack(pady=5, fill="both") # need the fill to make the anchor work
text2.pack(pady=5, fill="both") # need the fill to make the anchor work
text3.pack(pady=5, fill="both") # need the fill to make the anchor work

# Run the application
property_demo_window.mainloop()
