from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text="The button was clicked", fg="red")
    myLabel.pack()

myButton = Button(root, text="Click me!", padx=50, pady=20, command=myClick, fg="red", bg="light grey")
myButton.pack()

root.mainloop()