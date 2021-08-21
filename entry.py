from tkinter import *

root = Tk()

e = Entry(root, width=50, bg="light grey", borderwidth=2)
e.insert(0, "Enter your name")
e.pack()

def myClick():
    myLabel = Label(root, text=e.get(), fg="red")
    myLabel.pack()

myButton = Button(root, text="Enter yout name", padx=50, pady=20, command=myClick, fg="red", bg="light grey")
myButton.pack()

root.mainloop()