'''
Assignment 2.3 A small lexicon of widgets - Part 3
Author: Paul Ring
github link: https://github.com/plr5034/Python_ADD-160/blob/main/assignment_2.3_widget_lexicon.py

Create an application for a coffee shop that demonstrates menu use:

1) Create the main application window and set its title using coffee_app_window = tk.Tk()
and coffee_app_window.title("Coffee Shop Menu").
2) Create the menu bar with menu_bar = tk.Menu(coffee_app_window) and configure the coffee_app_window
window to use this menu bar with coffee_app_window.config(menu=menu_bar).
3) Create three menus for drinks, donuts, and bagels using tk.Menu(menu_bar,
tearoff=0).
4) Add the menus to the menu bar using menu_bar.add_cascade(label="MenuName",
menu=menu_name) and add commands inside the menus using 
menu_name.add_command(label="Show Menu", command=show_function).
5) Define functions show_drinks(), show_donuts(), and show_bagels() to display
the corresponding menu pages. Each function should:
    * Destroy any existing frames in the window using for widget in 
coffee_app_window.winfo_children(): if isinstance(widget, tk.Frame): 
widget.destroy().
    * Create a new frame using frame_name = tk.Frame(coffee_app_window) and
pack it using frame_name.pack(padx=10, pady=10).
    * Add labels and dropdowns for the number of items using tk.Label
(frame_name, text="LabelText").grid(row=row, column=column) 
    
Additionally, 
9) Implement Menus: Complete the donuts and bagels pages with a few choices
each.
10) Add Prices: Modify the code to include prices for the donuts and bagels.
Calculate the total order price and display it in the order summary. 
'''

# Importing necessary modules
import tkinter as tk
from tkinter import messagebox

# 1) Create the main application window and set its title using 
# coffee_app_window = tk.Tk() and coffee_app_window.title("Coffee Shop Menu").
coffee_app_window = tk.Tk()
coffee_app_window.title("Coffee Shop Menu")
# Set the window size as without it, the windows looks odd, 
# though it did resize for the menus.
coffee_app_window.geometry("350x350")  # Width x Height

def about_help():
    '''
    Function to display help information.
    
    Args:
        None
    Returns:
        None.
    '''
    messagebox.showinfo("Help",
                        "This is a placeholder")

def about_app():
    '''
    Function to display information about the application.
    '''
    messagebox.showinfo("About Coffee Shop Menupp",
                        "The application will allow a \nuser to select items sold in \nthe coffee shop and presents \nthe order and cost when done.\n\nVersion: 0.9 Beta")

def quit_dialog(event=None):
    '''
    Function to confirm if the user wants to quit the application.
    
    Args:
        None
    Returns:
        None
    '''
    if messagebox.askyesno("", "Are you sure you want to quit the App?"):
        coffee_app_window.destroy()

# 2) Create the menu bar with menu_bar = tk.Menu(coffee_app_window) and
# configure the coffee_app_window window to use this menu bar with
# coffee_app_window.config(menu=menu_bar).
menu_bar = tk.Menu(coffee_app_window)
coffee_app_window.config(menu=menu_bar)

# Variables to store order details
num_coffees = tk.IntVar(value=0)
num_cream = tk.IntVar(value=0)
num_sugar = tk.IntVar(value=0)
num_teas = tk.IntVar(value=0)
num_lemon = tk.IntVar(value=0)
num_honey = tk.IntVar(value=0)
num_premium_donuts = tk.IntVar(value=0)
num_plain_donuts = tk.IntVar(value=0)
num_glazed_donuts = tk.IntVar(value=0)
num_cronut_donuts = tk.IntVar(value=0)
num_chocolate_glazed_donuts = tk.IntVar(value=0)
num_donuts = tk.IntVar(value=0)
num_plain_bagels = tk.IntVar(value=0)
num_premium_bagels = tk.IntVar(value=0)
num_everything_bagels = tk.IntVar(value=0)
num_onion_bagels = tk.IntVar(value=0)
num_asiago_bagels = tk.IntVar(value=0)
num_bagels = tk.IntVar(value=0)

# 5) Define functions show_drinks(), show_donuts(), and show_bagels() to 
# display the corresponding menu pages.   Also, include additional requrements
# noted in the docstring.
# Step 2: Create Menus

def show_drinks():
    '''
    Function to display the drinks menu.

    This function displays the corresponding menu pages and also:
    * Destroy any existing frames in the window using for widget in 
    coffee_app_window.winfo_children(): if isinstance(widget, tk.Frame): 
    widget.destroy().
    * Create a new frame using frame_name = tk.Frame(coffee_app_window) and
    pack it using frame_name.pack(padx=10, pady=10).
    * Add labels and dropdowns for the number of items using tk.Label
    (frame_name, text="LabelText").grid(row=row, column=column) 
    
    Args:
        None
    Returns:
        None
    '''
    for widget in coffee_app_window.winfo_children():
        if isinstance(widget, tk.Frame):
            widget.destroy()
    drinks_frame = tk.Frame(coffee_app_window)
    drinks_frame.pack(padx=10, pady=10)

    tk.Label(drinks_frame, text="Number of Coffees:").grid(row=0, column=0, padx=10, pady=5)
    tk.OptionMenu(drinks_frame, num_coffees, *range(11)).grid(row=0, column=1, padx=10, pady=5)

    tk.Label(drinks_frame, text="Number of Cream:").grid(row=1, column=0, padx=10, pady=5)
    tk.OptionMenu(drinks_frame, num_cream, *range(11)).grid(row=1, column=1, padx=10, pady=5)

    tk.Label(drinks_frame, text="Number of Sugar:").grid(row=2, column=0, padx=10, pady=5)
    tk.OptionMenu(drinks_frame, num_sugar, *range(11)).grid(row=2, column=1, padx=10, pady=5)

    tk.Label(drinks_frame, text="Number of Teas:").grid(row=3, column=0, padx=10, pady=5)
    tk.OptionMenu(drinks_frame, num_teas, *range(11)).grid(row=3, column=1, padx=10, pady=5)

    tk.Label(drinks_frame, text="Number of Lemon:").grid(row=4, column=0, padx=10, pady=5)
    tk.OptionMenu(drinks_frame, num_lemon, *range(11)).grid(row=4, column=1, padx=10, pady=5)

    tk.Label(drinks_frame, text="Number of Honey:").grid(row=5, column=0, padx=10, pady=5)
    tk.OptionMenu(drinks_frame, num_honey, *range(11)).grid(row=5, column=1, padx=10, pady=5)

def show_donuts():
    '''
    Function to display the donuts menu.

    This function displays the corresponding menu pages and also:
    * Destroy any existing frames in the window using for widget in 
    coffee_app_window.winfo_children(): if isinstance(widget, tk.Frame): 
    widget.destroy().
    * Create a new frame using frame_name = tk.Frame(coffee_app_window) and
    pack it using frame_name.pack(padx=10, pady=10).
    * Add labels and dropdowns for the number of items using tk.Label
    (frame_name, text="LabelText").grid(row=row, column=column) 

    Args:
        None
    Returns:
        None
    '''
    for widget in coffee_app_window.winfo_children():
        if isinstance(widget, tk.Frame):
            widget.destroy()
    donuts_frame = tk.Frame(coffee_app_window)
    donuts_frame.pack(padx=10, pady=10)

    tk.Label(donuts_frame,
             text="Number of Plain Donuts:").grid(row=0, column=0, padx=10, pady=5)
    tk.OptionMenu(donuts_frame,
                  num_plain_donuts, *range(11)).grid(row=0, column=1, padx=10, pady=5)

    tk.Label(donuts_frame,
             text="Number of Glazed Donuts:").grid(row=1, column=0, padx=10, pady=5)
    tk.OptionMenu(donuts_frame,
                  num_glazed_donuts, *range(11)).grid(row=1, column=1, padx=10, pady=5)

    tk.Label(donuts_frame,
             text="Number of Cronut Donuts:").grid(row=2, column=0, padx=10, pady=5)
    tk.OptionMenu(donuts_frame,
                  num_cronut_donuts, *range(11)).grid(row=2, column=1, padx=10, pady=5)

    tk.Label(donuts_frame,
             text="Number of Chocolate Glazed Donuts:").grid(row=3, column=0, padx=10, pady=5)
    tk.OptionMenu(donuts_frame,
                  num_chocolate_glazed_donuts, *range(11)).grid(row=3, column=1, padx=10, pady=5)

def show_bagels():
    '''
    Function to display the bagels menu.

    This function displays the corresponding menu pages and also:
    * Destroy any existing frames in the window using for widget in 
    coffee_app_window.winfo_children(): if isinstance(widget, tk.Frame): 
    widget.destroy().
    * Create a new frame using frame_name = tk.Frame(coffee_app_window) and
    pack it using frame_name.pack(padx=10, pady=10).
    * Add labels and dropdowns for the number of items using tk.Label
    (frame_name, text="LabelText").grid(row=row, column=column) 

    Args:
        None
    Returns:
        None
    '''
    for widget in coffee_app_window.winfo_children():
        if isinstance(widget, tk.Frame):
            widget.destroy()
    bagels_frame = tk.Frame(coffee_app_window)
    bagels_frame.pack(padx=10, pady=10)

    tk.Label(bagels_frame, text="Number of Plain Bagels:").grid(row=0, column=0, padx=10, pady=5)
    tk.OptionMenu(bagels_frame, num_plain_bagels, *range(11)).grid(row=0, column=1, padx=10, pady=5)
    tk.Label(bagels_frame, text="Number of Everything Bagels:").grid(row=1, column=0, padx=10, pady=5)
    tk.OptionMenu(bagels_frame, num_everything_bagels, *range(11)).grid(row=1, column=1, padx=10, pady=5)
    tk.Label(bagels_frame, text="Number of Onion Bagels:").grid(row=2, column=0, padx=10, pady=5)
    tk.OptionMenu(bagels_frame, num_onion_bagels, *range(11)).grid(row=2, column=1, padx=10, pady=5)
    tk.Label(bagels_frame, text="Number of Asiago Bagels:").grid(row=3, column=0, padx=10, pady=5)
    tk.OptionMenu(bagels_frame, num_asiago_bagels, *range(11)).grid(row=3, column=1, padx=10, pady=5)

# Menu starts with "File" so have means to quit via standard interface.
# call are_you_sure() to confirm if the user wants to quit the application and
# to preform any clean up if needed.

sub_menu_file = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File",
                     menu=sub_menu_file,
                     underline=0)
sub_menu_file.add_command(label="Quit",
                          accelerator="Ctrl-Q",
                          underline=0,
                          command=quit_dialog)

# 3) Create three menus for drinks, donuts, and bagels using
#  tk.Menu(menu_bar,tearoff=0).
drinks_menu = tk.Menu(menu_bar, tearoff=0)
donuts_menu = tk.Menu(menu_bar, tearoff=0)
bagels_menu = tk.Menu(menu_bar, tearoff=0)

# 4) Add the menus to the menu bar using
# menu_bar.add_cascade(label="MenuName", menu=menu_name) and add commands
# inside the menus using menu_name.add_command(label="Show Menu",
# command=show_function).
menu_bar.add_cascade(label="Drinks", menu=drinks_menu)
menu_bar.add_cascade(label="Donuts", menu=donuts_menu)
menu_bar.add_cascade(label="Bagels", menu=bagels_menu)

# Add menu items and assign commands to the menus
drinks_menu.add_command(label="Show Drinks", command=show_drinks)
donuts_menu.add_command(label="Show Donuts", command=show_donuts)
bagels_menu.add_command(label="Show Bagels", command=show_bagels)

# Add an about menu
sub_menu_help = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help",
                     menu=sub_menu_help,
                     underline=0)
sub_menu_help.add_command(label="Help",
                          command=about_help,
                          underline=0)
sub_menu_help.add_command(label="About...",
                          command=about_app,
                          underline=0)

# Function to display the order summary
def show_order():
    '''
    Function to display the Users order.

    This function displays a message box with the order summary and total
    cost.

    Args:
        None
    Returns:
        None
    '''
    num_premium_donuts.set(num_glazed_donuts.get() \
                 + num_cronut_donuts.get() \
                 + num_chocolate_glazed_donuts.get())
    num_donuts.set(num_plain_donuts.get() + num_premium_donuts.get())
    num_premium_bagels.set(num_everything_bagels.get() \
                 + num_onion_bagels.get() \
                 + num_asiago_bagels.get())
    num_bagels.set(num_plain_bagels.get() + num_everything_bagels.get())
    total_cost = num_coffees.get() * 2 \
               + num_teas.get() * 2 \
               + num_plain_donuts.get() * 1 \
               + num_premium_donuts.get() * 1.5 \
               + num_bagels.get() * 1 \
               + num_premium_bagels.get() * 1.5
    order = (f"Coffees: {num_coffees.get()}, Cream: {num_cream.get()}, Sugar: {num_sugar.get()}\n"
             f"Teas: {num_teas.get()}, Lemon: {num_lemon.get()}, Honey: {num_honey.get()}\n"
             f"Donuts: {num_donuts.get()}\n"
             f"Bagels: {num_bagels.get()}\n"
             f"Total Cost: ${total_cost:.2f}")
    messagebox.showinfo("Order Summary", order)

# Create a Button to complete the order
complete_order_button = tk.Button(coffee_app_window, text="Complete Order", command=show_order)
complete_order_button.pack(pady=10)

# This will bind the Ctrl-q to quit
coffee_app_window.bind_all("<Control-q>", quit_dialog)
# Run the application
coffee_app_window.mainloop()