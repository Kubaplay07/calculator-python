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
def button1_press(event):
    button_press(1)

def button2_press(event):
    button_press(2)

def button3_press(event):
    button_press(3)

def button4_press(event):
    button_press(4)

def button5_press(event):
    button_press(5)

def button6_press(event):
    button_press(6)

def button7_press(event):
    button_press(7)

def button8_press(event):
    button_press(8)

def button9_press(event):
    button_press(9)

def button0_press(event):
    button_press(0)

# Define the operations
def button_add_press(event):
    first_number = entry.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    entry.delete(0, tk.END)

def button_sub_press(event):
    first_number = entry.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    entry.delete(0, tk.END)

def button_mul_press(event):
    first_number = entry.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    entry.delete(0, tk.END)

def button_div_press(event):
    first_number = entry.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    entry.delete(0, tk.END)

# Define the clear function
def button_clear_press(event):
    entry.delete(0, tk.END)

# Define the calculation function
def button_calc_press(event):
    second_number = entry.get()
    entry.delete(0, tk.END)

    if math == "addition":
        result = f_num + int(second_number)
    elif math == "subtraction":
        result = f_num - int(second_number)
    elif math == "multiplication":
        result = f_num * int(second_number)
    elif math == "division":
        result = f_num / int(second_number)

    entry.insert(0, result)





# Tell the buttons what to do when they are pressed
button1.bind('<Button-1>', button1_press)
button2.bind('<Button-1>', button2_press)
button3.bind('<Button-1>', button3_press)
button4.bind('<Button-1>', button4_press)
button5.bind('<Button-1>', button5_press)
button6.bind('<Button-1>', button6_press)
button7.bind('<Button-1>', button7_press)
button8.bind('<Button-1>', button8_press)
button9.bind('<Button-1>', button9_press)
button0.bind('<Button-1>', button0_press)
button_add.bind('<Button-1>', button_add_press)
button_sub.bind('<Button-1>', button_sub_press)
button_mul.bind('<Button-1>', button_mul_press)
button_div.bind('<Button-1>', button_div_press)
button_calc.bind('<Button-1>', button_calc_press)
button_clear.bind('<Button-1>', button_clear_press)





# # F scalable program
# # Define the button labels and their corresponding press functions
# buttons = [    ('1', button1_press),    ('2', button2_press),    ('3', button3_press),    ('4', button4_press),    ('5', button5_press),    ('6', button6_press),    ('7', button7_press),    ('8', button8_press),    ('9', button9_press),    ('0', button0_press),    ('+', button_add_press),    ('-', button_sub_press),    ('*', button_mul_press),    ('/', button_div_press),    ('=', button_calc_press),    ('AC', button_clear_press),]

# # Define the button grid layout
# for i, (label, press_func) in enumerate(buttons):
#     button = tk.Button(window, text=label)
#     button.grid(row=i // 1, column=i % 1)
#     button.bind('<Button-1>', press_func)





# Start the main loop
window.mainloop()





#