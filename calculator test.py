from tkinter import *

root = Tk()

display = Entry(root, width=50, f)
display.grid(row=0, columnspan=3)

def calcButton(val):
    newVal = str(display.get()) + str(val)
    display.insert(0, newVal)

buttonOne = Button(root, text="1", pady=25, padx=25, command=calcButton)
buttonTwo = Button(root, text="2", pady=25, padx=25, command=calcButton(2))
buttonThree = Button(root, text="3", pady=25, padx=25, command=calcButton(3))
buttonFour = Button(root, text="4", pady=25, padx=25, command=calcButton(4))
buttonFive = Button(root, text="5", pady=25, padx=25, command=calcButton(5))
buttonSix = Button(root, text="6", pady=25, padx=25, command=calcButton(6))
buttonSeven = Button(root, text="7", pady=25, padx=25, command=calcButton(7))
buttonEight = Button(root, text="8", pady=25, padx=25, command=calcButton(8))
buttonNine = Button(root, text="9", pady=25, padx=25, command=calcButton(9))
buttonZero = Button(root, text="0", pady=25, padx=25, command=calcButton(0))
buttonplus = Button(root, text="+", pady=25, padx=25)
buttonEquals = Button(root, text="=", pady=25, padx=25)

buttonOne.grid(row=3 , column=0)
buttonTwo.grid(row=3 , column=1)
buttonThree.grid(row=3 , column=2)
buttonFour.grid(row=2 , column=0)
buttonFive.grid(row=2 , column=1)
buttonSix.grid(row=2 , column=2)
buttonSeven.grid(row=1 , column=0)
buttonEight.grid(row=1 , column=1)
buttonNine.grid(row=1 , column=2)
buttonZero.grid(row=4 , column=0)
buttonplus.grid(row=4 , column=1)
buttonEquals.grid(row=4 , column=2)

root.mainloop()