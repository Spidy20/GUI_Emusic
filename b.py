import tkinter
from  tkinter import *
root = Tk()
image = PhotoImage(file="button.gif")
for _ in range(5):
    Button(root, image=image, borderwidth=0, relief=SUNKEN).pack()
root.mainloop()