import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    expression = entry.get()
    result = eval(expression)
    entry.delete(0, tk.END)
    entry.insert(tk.END, result)

# Create the main window
window = tk.Tk()
window.title("Calculator")

# Create the entry field
entry = tk.Entry(window, width=30)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define the buttons
buttons = [
    ("C", 1, 3),
    ("7", 2, 0),
    ("8", 2, 1),
    ("9", 2, 2),
    ("/", 2, 3),
    ("4", 3, 0),
    ("5", 3, 1),
    ("6", 3, 2),
    ("*", 3, 3),
    ("1", 4, 0),
    ("2", 4, 1),
    ("3", 4, 2),
    ("-", 4, 3),
    ("0", 5, 0),
    (".", 5, 1),
    ("=", 5, 2),
    ("+", 5, 3)
]

# Create the buttons and assign their respective functions
for button_text, row, column in buttons:
    button = tk.Button(window, text=button_text, padx=20, pady=10)
    button.grid(row=row, column=column, padx=5, pady=5)

    if button_text == "=":
        button.config(command=button_equal)
    elif button_text == "C":
        button.config(command=button_clear)
    else:
        button.config(command=lambda num=button_text: button_click(num))

# Start the main loop
window.mainloop()
