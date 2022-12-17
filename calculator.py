import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.configure(bg='#212121')
        self.root.title('Calculator')
        self.root.geometry('300x400')

        # Initialize the display frame
        self.display_frame = tk.Frame(self.root, bg='#212121', height=100, width=300)
        self.display_frame.pack(side='top')

        # Initialize the display label
        self.display = tk.Label(self.display_frame, text='0', bg='#424242', fg='#FFFFFF', font=('Helvetica', 24), anchor='e', width=16, height=2)
        self.display.pack(side='top')

        # Initialize the number buttons frame
        self.number_buttons_frame = tk.Frame(self.root, bg='#212121', height=300, width=225)
        self.number_buttons_frame.pack(side='left')

        # Initialize the number buttons
        
        self.button_1 = tk.Button(self.number_buttons_frame, text='1', bg='#424242', fg='#FFFFFF', font=('Helvetica', 18), width=5, height=2, command=lambda: self.append_number('1'))
        self.button_1.grid(row=2, column=0)

        self.button_2 = tk.Button(self.number_buttons_frame, text='2', bg='#424242', fg='#FFFFFF', font=('Helvetica', 18), width=5, height=2, command=lambda: self.append_number('2'))
        self.button_2.grid(row=2, column=1)

        self.button_3 = tk.Button(self.number_buttons_frame, text='3', bg='#424242', fg='#FFFFFF', font=('Helvetica', 18), width=5, height=2, command=lambda: self.append_number('3'))
        self.button_3.grid(row=2, column=2)
        
        self.button_4 = tk.Button(self.number_buttons_frame, text='4', bg='#424242', fg='#FFFFFF', font=('Helvetica', 18), width=5, height=2, command=lambda: self.append_number('4'))
        self.button_4.grid(row=1, column=0)

        self.button_5 = tk.Button(self.number_buttons_frame, text='5', bg='#424242', fg='#FFFFFF', font=('Helvetica', 18), width=5, height=2, command=lambda: self.append_number('5'))
        self.button_5.grid(row=1, column=1)

        self.button_6 = tk.Button(self.number_buttons_frame, text='6', bg='#424242', fg='#FFFFFF', font=('Helvetica', 18), width=5, height=2, command=lambda: self.append_number('6'))
        self.button_6.grid(row=1, column=2)

        self.button_7 = tk.Button(self.number_buttons_frame, text='7', bg='#424242', fg='#FFFFFF', font=('Helvetica', 18), width=5, height=2, command=lambda: self.append_number('7'))
        self.button_7.grid(row=0, column=0)

        self.button_8 = tk.Button(self.number_buttons_frame, text='8', bg='#424242', fg='#FFFFFF', font=('Helvetica', 18), width=5, height=2, command=lambda: self.append_number('8'))
        self.button_8.grid(row=0, column=1)

        self.button_9 = tk.Button(self.number_buttons_frame, text='9', bg='#424242', fg='#FFFFFF', font=('Helvetica', 18), width=5, height=2, command=lambda: self.append_number('9')) 
        self.button_9.grid(row=0, column=2)

        self.button_0 = tk.Button(self.number_buttons_frame, text='0', bg='#424242', fg='#FFFFFF', font=('Helvetica', 18), width=5, height=2, command=lambda: self.append_number('0'))
        self.button_0.grid(row=3, column=0)

        self.button_decimal = tk.Button(self.number_buttons_frame, text='.', bg='#424242', fg='#FFFFFF', font=('Helvetica', 18), width=5, height=2, command=lambda: self.append_number('.'))
        self.button_decimal.grid(row=3, column=1)

        self.button_clear = tk.Button(self.number_buttons_frame, text='C', bg='#424242', fg='#FFFFFF', font=('Helvetica', 18), width=5, height=2, command=lambda: self.clear_display())
        self.button_clear.grid(row=3, column=2)

        # Initialize the operator buttons frame
        self.operator_buttons_frame = tk.Frame(self.root, bg='#212121', height=300, width=75)
        self.operator_buttons_frame.pack(side='right')

        # Initialize the operator buttons
        self.button_divide = tk.Button(self.operator_buttons_frame, text='/', bg='#212121', fg='#FFFFFF', font=('Helvetica', 18), width=5, height=2, command=lambda: self.append_operator('/'))
        self.button_divide.pack(side='top')

        self.button_subtract = tk.Button(self.operator_buttons_frame, text='-', bg='#212121', fg='#FFFFFF', font=('Helvetica', 18), width=5, height=2, command=lambda: self.append_operator('-'))
        self.button_subtract.pack(side='top')

        self.button_add = tk.Button(self.operator_buttons_frame, text='+', bg='#212121', fg='#FFFFFF', font=('Helvetica', 18), width=5, height=2, command=lambda: self.append_operator('+'))
        self.button_add.pack(side='top')

        self.button_equals = tk.Button(self.operator_buttons_frame, text='=', bg='#212121', fg='#FFFFFF', font=('Helvetica', 18), width=5, height=2, command=lambda: self.calculate())
        self.button_equals.pack(side='bottom')

    def append_number(self, number):
        # Append the number to the display
        current_text = self.display.cget('text')
        if current_text == '0':
            self.display.config(text=number)
        else:
            self.display.config(text=current_text + number)

    def append_operator(self, operator):
        # Append the operator to the display
        current_text = self.display.cget('text')
        self.display.config(text=current_text + operator)

    def clear_display(self):
        # Reset the display to zero
        self.display.config(text='0')

    def calculate(self):
        # Calculate the result of the expression
        try:
            result = eval(self.display.cget('text'))
            self.display.config(text=str(result))
        except Exception:
            self.display.config(text='Error')

if __name__ == '__main__':
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
