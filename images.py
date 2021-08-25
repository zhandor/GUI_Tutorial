from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Images and Icons')
root.iconbitmap('C:/Users/zhand/Projetos/Python/GUI_Tutorial/icons/pythonblue.icon.ico')

my_img = ImageTk.PhotoImage(Image.open('C:/Users/zhand/Projetos/Python/GUI_Tutorial/icons/python.logo.png'))

my_label = Label(image=my_img)

my_label.pack()

quit_button = Button(root, text='fechar', command=root.quit)
quit_button.pack()

root.mainloop()