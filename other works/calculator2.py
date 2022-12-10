import tkinter as tk

# Define the main window
window = tk.Tk()

# Define the buttons for the calculator
button1 = tk.Button(window, text='1')
button2 = tk.Button(window, text='2')
button3 = tk.Button(window, text='3')
button4 = tk.Button(window, text='4')
button5 = tk.Button(window, text='5')
button6 = tk.Button(window, text='6')
button7 = tk.Button(window, text='7')
button8 = tk.Button(window, text='8')
button9 = tk.Button(window, text='9')
button0 = tk.Button(window, text='0')
button_add = tk.Button(window, text='+')
button_sub = tk.Button(window, text='-')
button_mul = tk.Button(window, text='*')
button_div = tk.Button(window, text='/')
button_calc = tk.Button(window, text='=')
button_clear = tk.Button(window, text='AC')

# Create a text entry box for the calculator
entry = tk.Entry(window, width=35)

# Define the button grid layout
button1.grid(row=1, column=0)
button2.grid(row=1, column=1)
button3.grid(row=1, column=2)
button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
button7.grid(row=3, column=0)
button8.grid(row=3, column=1)
button9.grid(row=3, column=2)
button0.grid(row=4, column=0)
button_add.grid(row=1, column=3)
button_sub.grid(row=2, column=3)
button_mul.grid(row=3, column=3)
button_div.grid(row=4, column=3)
button_calc.grid(row=4, column=2)
button_clear.grid(row=4, column=1)

# Put the text entry box on the screen
entry.grid(row=0, column=0, columnspan=4)

# Define the function for each button press
def button_press(number):
    # Get the current value in the entry field
    current = entry.get()
    # Delete the current value and insert the new one
    entry.delete(0, tk.END)
    entry.insert(0, str(current) + str(number))

# Define a function for each button
def button1_press():
    button_press(1)

def button2_press():
    button_press(2)

def button3_press():
    button_press(3)

def button4_press():
    button_press(4)

def button5_press():
    button_press(5)

def button6_press():
    button_press(6)

def button7_press():
    button_press(7)

def button8_press():
    button_press(8)

def button9_press():
    button_press(9)

def button0_press():
    button_press(0)

# Define the operations
def button_add_press():
    first_number = entry.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    entry.delete(0, tk.END)

def button_sub_press():
    first_number = entry.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    entry.delete(0, tk.END)

def button_mul_press():
    first_number = entry.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    entry.delete(0, tk.END)

def button_div_press():
    first_number = entry.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    entry.delete(0, tk.END)

# Define the Clear button
def button_clear_press():
    entry.delete(0, tk.END)

# Define the Equal button
def button_equal_press():
    second_number = entry.get()
    entry.delete(0, tk.END)

    if math == "addition":
        entry.insert(0, f_num + int(second_number))

    if math == "subtraction":
        entry.insert(0, f_num - int(second_number))

    if math == "multiplication":
        entry.insert(0, f_num * int(second_number))

    if math == "division":
        entry.insert(0, f_num / int(second_number))

# Tell the buttons what to do when they are clicked
button1.configure(command=button1_press)
button2.configure(command=button2_press)
button3.configure(command=button3_press)
button4.configure(command=button4_press)
button5.configure(command=button5_press)
button6.configure(command=button6_press)
button7.configure(command=button7_press)
button8.configure(command=button8_press)
button9.configure(command=button9_press)
button0.configure(command=button0_press)
button_add.configure(command=button_add_press)
button_sub.configure(command=button_sub_press)
button_mul.configure(command=button_mul_press)
button_div.configure(command=button_div_press)

# Tell the buttons what to do when they are clicked
button1.configure(command=button1_press)
button2.configure(command=button2_press)
button3.configure(command=button3_press)
button4.configure(command=button4_press)
button5.configure(command=button5_press)
button6.configure(command=button6_press)
button7.configure(command=button7_press)
button8.configure(command=button8_press)
button9.configure(command=button9_press)
button0.configure(command=button0_press)
button_add.configure(command=button_add_press)
button_sub.configure(command=button_sub_press)
button_mul.configure(command=button_mul_press)
button_div.configure(command=button_div_press)
button_calc.configure(command=button_equal_press)
button_clear.configure(command=button_clear_press)

# Start the GUI
window.mainloop()
