import tkinter as tk
import math

# Define the main window
window = tk.Tk()

# Define the buttons for the calculator
buttons = [
    "1", "2", "3",
    "4", "5", "6",
    "7", "8", "9",
    "0", "+", "-",
    "*", "/", "=",
    "AC", "sqrt"
]

# Create a dictionary of operations and their corresponding functions
operations = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y,
    "sqrt": lambda x: math.sqrt(x)
}

# Create a text entry box for the calculator
entry = tk.Entry(window, width=35)
entry.pack()

# Define the function for each button press
def button_press(button):
    # Get the current value in the entry field
    current = entry.get()

    # Clear the entry field and update the value based on the button press
    if button == "AC":
        entry.delete(0, tk.END)
    elif button in operations:
        # Save the current value and the operation
        global f_num
        global operation
        f_num = int(current)
        operation = button
        entry.delete(0, tk.END)
    elif button == "=":
        # Calculate the result and display it in the entry field
        if operation in operations:
            result = operations[operation](f_num, int(current))
            entry.delete(0, tk.END)
            entry.insert(0, result)
        else:
            result = operations[operation](f_num)
            entry.delete(0, tk.END)
            entry.insert(0, result)
    else:
        # Update the entry field with the new value
        entry.delete(0, tk.END)
        entry.insert(0, str(current) + str(button))

# Create a button for each item in the buttons list
for button in buttons:
    tk.Button(window, text=button, command=lambda b=button: button_press(b)).pack()

# Start the main event loop
window.mainloop()
