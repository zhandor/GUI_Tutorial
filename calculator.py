from tkinter import *

root = Tk()
root.title("Simple Calculator")

display = Entry(root, width=35, borderwidth=5)
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def calcButton(val):
    return val
    # newVal = str(display.get()) + str(val)
    # display.insert(0, newVal)

button_1 = Button(root, text="1", width=5, height=2, command=calcButton)
button_2 = Button(root, text="2", width=5, height=2, command=calcButton)
button_3 = Button(root, text="3", width=5, height=2, command=calcButton)
button_4 = Button(root, text="4", width=5, height=2, command=calcButton)
button_5 = Button(root, text="5", width=5, height=2, command=calcButton)
button_6 = Button(root, text="6", width=5, height=2, command=calcButton)
button_7 = Button(root, text="7", width=5, height=2, command=calcButton)
button_8 = Button(root, text="8", width=5, height=2, command=calcButton)
button_9 = Button(root, text="9", width=5, height=2, command=calcButton)
button_0 = Button(root, text="0", width=15, height=2, command=calcButton)

button_add = Button(root, text="+", width=5, height=2)
button_equals = Button(root, text="=", width=5, height=6)
button_clear = Button(root, text="Clear", width=5, height=2)

button_1.grid(row=3 , column=0)
button_2.grid(row=3 , column=1)
button_3.grid(row=3 , column=2)
button_equals.grid(row=3 , column=3, rowspan=2)

button_4.grid(row=2 , column=0)
button_5.grid(row=2 , column=1)
button_6.grid(row=2 , column=2)
button_add.grid(row=2 , column=3)

button_7.grid(row=1 , column=0)
button_8.grid(row=1 , column=1)
button_9.grid(row=1 , column=2)
button_clear.grid(row=1, column=3)

button_0.grid(row=4 , column=0, columnspan=3)

root.mainloop()