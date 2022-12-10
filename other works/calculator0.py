import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Calculator")

# Create the input fields
input_field1 = tk.Entry(window)
input_field2 = tk.Entry(window)

# Create the output field
output_field = tk.Text(window)

# Create the buttons
button_plus = tk.Button(window, text="+")
button_minus = tk.Button(window, text="-")
button_times = tk.Button(window, text="*")
button_divide = tk.Button(window, text="/")

# Arrange the elements on the screen using a grid layout
input_field1.grid(row=0, column=0)
input_field2.grid(row=1, column=0)
output_field.grid(row=2, column=0)
button_plus.grid(row=0, column=1)
button_minus.grid(row=1, column=1)
button_times.grid(row=2, column=1)
button_divide.grid(row=3, column=1)

# Run the main loop
window.mainloop()
