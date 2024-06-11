import tkinter
from tkinter import *
 
root = Tk() 
a = Label(root, text ="Hello World") 
a.pack() 
  
root.mainloop() 

from tkinter import *
# create root window
root = Tk()
 
# root window title and dimension
root.title("Welcome to GeekForGeeks")
# Set geometry (widthxheight)
root.geometry('350x200')
 
# all widgets will be here
# Execute Tkinter
root.mainloop()

# import required module 
from tkinter import *

# create object 
root = Tk() 

# create button to implement destroy() 
Button(root, text="Quit", command=root.destroy).pack() 

root.mainloop() 

# Basic Widgets in Tkinter:
# (1.) Label 

import tkinter as tk

# Create the main window
root = tk.Tk()
root.geometry("400x250")  # Set window size
root.title("Welcome to My App")  # Set window title

# Create a StringVar to associate with the label
text_var = tk.StringVar()
text_var.set("Hello, World!")

# Create the label widget with all options
label = tk.Label(root, 
                 textvariable=text_var, 
                 anchor=tk.CENTER,       
                 bg="lightblue",      
                 height=3,              
                 width=30,              
                 bd=3,                  
                 font=("Arial", 16, "bold"), 
                 cursor="hand2",   
                 fg="red",             
                 padx=15,               
                 pady=15,                
                 justify=tk.CENTER,    
                 relief=tk.RAISED,     
                 underline=0,           
                 wraplength=250         
                )

# Pack the label into the window
label.pack(pady=20)  # Add some padding to the top


# Run the main event loop
root.mainloop()

# (2.) Button

import tkinter as tk

def button_clicked():
    print("Button clicked!")

root = tk.Tk()

# Creating a button with specified options
button = tk.Button(root, 
                   text="Click Me", 
                   command=button_clicked,
                   activebackground="blue", 
                   activeforeground="white",
                   anchor="center",
                   bd=3,
                   bg="lightgray",
                   cursor="hand2",
                   disabledforeground="gray",
                   fg="black",
                   font=("Arial", 12),
                   height=2,
                   highlightbackground="black",
                   highlightcolor="green",
                   highlightthickness=2,
                   justify="center",
                   overrelief="raised",
                   padx=10,
                   pady=5,
                   width=15,
                   wraplength=100)

button.pack(padx=20, pady=20)

root.mainloop()

# (3.) Entry
# creating a simple tkinter window

import tkinter as tk
root = tk.Tk()
root.title("First Tkinter Window")
root.mainloop()

# (4.) Frame

import tkinter as tk
# Function to create widgets with all options
def create_widget(parent, widget_type, **options):
    return widget_type(parent, **options)

# Create the main window
window = create_widget(None, tk.Tk)
window.title("GUI Example")

# Create a Frame widget with all options
frame = create_widget(window, tk.Frame, bg='lightblue', bd=3, cursor='hand2', height=100, 
                      highlightcolor='red', highlightthickness=2, highlightbackground='black', 
                      relief=tk.RAISED, width=200)
frame.pack(padx=20, pady=20)
window.mainloop()

# (5.) Checkbutton
import tkinter as tk

def on_button_toggle():
    if var.get() == 1:
        print("Checkbutton is selected")
    else:
        print("Checkbutton is deselected")

root = tk.Tk()

# Creating a Checkbutton
var = tk.IntVar()
checkbutton = tk.Checkbutton(root, text="Enable Feature", variable=var, 
                             onvalue=1, offvalue=0, command=on_button_toggle)

# Setting options for the Checkbutton
checkbutton.config(bg="lightgrey", fg="blue", font=("Arial", 12), 
                   selectcolor="green", relief="raised", padx=10, pady=5)

# Adding a bitmap to the Checkbutton
checkbutton.config(bitmap="info", width=20, height=2)

# Placing the Checkbutton in the window
checkbutton.pack(padx=40, pady=40)

# Calling methods on the Checkbutton
checkbutton.flash()

root.mainloop()

# (6.) RadioButtton

# Importing Tkinter module
from tkinter import *
# from tkinter.ttk import *

# Creating master Tkinter window
master = Tk()
master.geometry("175x175")

# Tkinter string variable
# able to store any string value
v = StringVar(master, "1")

# Dictionary to create multiple buttons
values = {"RadioButton 1" : "1",
		"RadioButton 2" : "2",
		"RadioButton 3" : "3",
		"RadioButton 4" : "4",
		"RadioButton 5" : "5"}

# Loop is used to create multiple Radiobuttons
# rather than creating each button separately
for (text, value) in values.items():
	Radiobutton(master, text = text, variable = v, 
				value = value, indicator = 0,
				background = "light blue").pack(fill = X, ipady = 5)

# Infinite loop can be terminated by
# keyboard or mouse interrupt
# or by any predefined function (destroy())
mainloop()

# (7.) Listbox

from tkinter import *

# create a root window.
top = Tk()

# create listbox object
listbox = Listbox(top, height = 10, 
				width = 15, 
				bg = "grey",
				activestyle = 'dotbox', 
				font = "Helvetica",
				fg = "yellow")

# Define the size of the window.
top.geometry("300x250") 

# Define a label for the list. 
label = Label(top, text = " FOOD ITEMS") 

# insert elements by their
# index and names.
listbox.insert(1, "Nachos")
listbox.insert(2, "Sandwich")
listbox.insert(3, "Burger")
listbox.insert(4, "Pizza")
listbox.insert(5, "Burrito")

# pack the widgets
label.pack()
listbox.pack()

# Display until User 
# exits themselves.
top.mainloop()

# (8.) ScrollBar
from tkinter import *

root = Tk() 
root.geometry("150x200") 

w = Label(root, text ='GeeksForGeeks', 
		font = "50") 

w.pack() 

scroll_bar = Scrollbar(root) 

scroll_bar.pack( side = RIGHT, 
				fill = Y ) 

mylist = Listbox(root, 
				yscrollcommand = scroll_bar.set ) 

for line in range(1, 26): 
	mylist.insert(END, "Geeks " + str(line)) 

mylist.pack( side = LEFT, fill = BOTH ) 

scroll_bar.config( command = mylist.yview ) 

root.mainloop() 

