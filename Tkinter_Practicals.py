# (1.) Create clickable buttons to trigger actions.

import tkinter as tk
def button_clicked():
    print("Button clicked!")
root = tk.Tk()

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

# (2.) Display dialog boxes for messages, warnings, etc.

from tkinter import *
from tkinter import messagebox 
root = Tk() 
root.geometry("300x200") 
w = Label(root, text ='Tkinter Practical', font = "50") 
w.pack() 

messagebox.showinfo("showinfo", "Information") 
messagebox.showwarning("showwarning", "Warning") 
messagebox.showerror("showerror", "Error") 
messagebox.askquestion("askquestion", "Are you sure?") 
messagebox.askokcancel("askokcancel", "Want to continue?") 
messagebox.askyesno("askyesno", "Find the value?") 
messagebox.askretrycancel("askretrycancel", "Try again?") 

root.mainloop() 

# (3.) Create a multiline text input with advanced editing capabilities..

import tkinter as tk
root = Tk()
root.geometry("250x170")
T = Text(root, height = 5, width = 52)
l = Label(root, text = "Fact of the Day")
l.config(font =("Courier", 14))

Fact = """A man without education is like a bird without wings"""

# Create button for next text.
b1 = Button(root, text = "Next", )

# Create an Exit button.
b2 = Button(root, text = "Exit",
			command = root.destroy) 

l.pack()
T.pack()
b1.pack()
b2.pack()

# Insert The Fact.
T.insert(tk.END, Fact)

tk.mainloop()
