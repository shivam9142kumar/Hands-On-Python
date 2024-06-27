import tkinter as tk

def on_button_click():
    label.config(text=f"Entry content: {entry.get()}")

# Create the main window
root = tk.Tk()
root.title("Basic Tkinter Widgets")

# Label
label = tk.Label(root, text="Hello, Tkinter!")
label.pack(pady=5)

# Button
button = tk.Button(root, text="Click Me", command=on_button_click)
button.pack(pady=5)

# Entry
entry = tk.Entry(root)
entry.pack(pady=5)

# Text
text = tk.Text(root, height=5, width=40)
text.pack(pady=5)

# Frame
frame = tk.Frame(root, borderwidth=2, relief="sunken")
frame.pack(pady=5, fill="x")
tk.Label(frame, text="Inside a Frame").pack()

# Checkbutton
check_var = tk.IntVar()
checkbutton = tk.Checkbutton(root, text="Check Me", variable=check_var)
checkbutton.pack(pady=5)

# Radiobutton
radio_var = tk.StringVar(value="Option 1")
radiobutton1 = tk.Radiobutton(root, text="Option 1", variable=radio_var, value="Option 1")
radiobutton2 = tk.Radiobutton(root, text="Option 2", variable=radio_var, value="Option 2")
radiobutton1.pack()
radiobutton2.pack()

# Listbox
listbox = tk.Listbox(root)
listbox.insert(1, "Item 1")
listbox.insert(2, "Item 2")
listbox.pack(pady=5)

# Scrollbar
scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Canvas
canvas = tk.Canvas(root, width=100, height=100, bg="white")
canvas.pack(pady=5)
canvas.create_oval(10, 10, 90, 90, fill="blue")

# Run the application
root.mainloop()
