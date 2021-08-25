from tkinter import *

root = Tk()
root.title("Simple Calculator")

display = Entry(root, width = 35, borderwidth = 5)
display.grid(row = 0, column = 0, columnspan = 4, padx = 10, pady = 10)

result = 0
lastOperation = ''

def button_click(number):
    newVal = str(display.get()) + str(number)    
    clear_display()
    fill_display(newVal)

def clear_display():
    global result    
    display.delete(0, END)

def clear_click():
    clear_display()
    global result
    result = 0

def run_last_operation():
    global lastOperation
    
    if(lastOperation == 'add'):
        add_click()
    elif(lastOperation == 'subtract'): 
        subtract_click()
    elif(lastOperation == 'multiply'): 
        multiply_click()
    elif(lastOperation == 'divide'): 
        divide_click()
    else:
        print('nenhuma operação em memória')
    lastOperation = ''

def add_click():
    global result, lastOperation

    currentVal = float(display.get())
    if(lastOperation == ''):
        result = currentVal
    else:
        currentResult = result
        result = float(currentResult) + currentVal

    lastOperation = 'add'
    
    clear_display()

def subtract_click():
    global result, lastOperation
    
    currentVal = float(display.get())
    if(lastOperation == ''):
        result = currentVal
    else:
        currentResult = result
        result = float(currentResult) - currentVal

    lastOperation = 'subtract'
    
    clear_display()

def multiply_click():
    global result, lastOperation
    
    currentVal = float(display.get())
    if(lastOperation == ''):
        result = currentVal
    else:
        currentResult = result
        result = float(currentResult) * currentVal

    lastOperation = 'multiply'

    clear_display()

def divide_click():
    global result, lastOperation
    
    currentVal = float(display.get())
    if(lastOperation == ''):
        result = currentVal
    else:
        currentResult = result
        result = float(currentResult) / currentVal

    lastOperation = 'divide'
    
    clear_display()

def fill_display(value):
    display.insert(0, value)

def equals_click():
    run_last_operation()
    global result
    fill_display(result)
    

button_1 = Button(root, text = "1", padx = 40,  pady = 20, command = lambda: button_click(1))
button_2 = Button(root, text = "2", padx = 40,  pady = 20, command = lambda: button_click(2))
button_3 = Button(root, text = "3", padx = 40,  pady = 20, command = lambda: button_click(3))
button_4 = Button(root, text = "4", padx = 40,  pady = 20, command = lambda: button_click(4))
button_5 = Button(root, text = "5", padx = 40,  pady = 20, command = lambda: button_click(5))
button_6 = Button(root, text = "6", padx = 40,  pady = 20, command = lambda: button_click(6))
button_7 = Button(root, text = "7", padx = 40,  pady = 20, command = lambda: button_click(7))
button_8 = Button(root, text = "8", padx = 40,  pady = 20, command = lambda: button_click(8))
button_9 = Button(root, text = "9", padx = 40,  pady = 20, command = lambda: button_click(9))
button_0 = Button(root, text = "0", padx = 135, pady = 20, command = lambda: button_click(0))

button_add      = Button(root, text = "+",      padx = 40, pady = 20, command = lambda: add_click())
button_subtract = Button(root, text = "-",      padx = 40, pady = 20, command = lambda: subtract_click())
button_multiply = Button(root, text = "*",      padx = 40, pady = 20, command = lambda: multiply_click())
button_divide   = Button(root, text = "/",      padx = 40, pady = 20, command = lambda: divide_click())
button_equals   = Button(root, text = "=",      padx = 85, pady = 20, command = lambda: equals_click())
button_clear    = Button(root, text = "Clear",  padx = 85, pady = 20, command = lambda: clear_click())

button_7.grid(row = 1 , column = 0)
button_8.grid(row = 1 , column = 1)
button_9.grid(row = 1 , column = 2)
button_clear.grid(row = 1, column = 3, columnspan=2)

button_4.grid(row = 2 , column = 0)
button_5.grid(row = 2 , column = 1)
button_6.grid(row = 2 , column = 2)
button_add.grid(row = 2 , column = 3)
button_subtract.grid(row = 2 , column = 4)

button_1.grid(row = 3 , column = 0)
button_2.grid(row = 3 , column = 1)
button_3.grid(row = 3 , column = 2)
button_multiply.grid(row = 3 , column = 3)
button_divide.grid(row = 3 , column = 4)

button_0.grid(row = 4 , column = 0, columnspan = 3)
button_equals.grid(row = 4 , column = 3, rowspan = 2)

root.mainloop()