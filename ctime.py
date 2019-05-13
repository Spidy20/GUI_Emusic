from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image

windo = Tk()
windo.iconbitmap('C:/Users/kusha/PycharmProjects/GUI Emusic/icons/music.ico')
windo.title("About Me")
windo.geometry('820x420')
windo.resizable(0, 0)

sub = tk.Label(windo, text="Name", width=9, height=1, fg="white", bg="blue2", font=('times', 19, ' bold '))
sub.place(x=305, y=100)

col = tk.Label(windo, text="College", width=9, height=1, fg="white", bg="blue2", font=('times', 19, ' bold '))
col.place(x=305, y=150)

dname = tk.Label(windo, text="Twaibu Songoro", width=15, height=1, fg="white", bg="lime green", font=('times', 19, ' bold '))
dname.place(x=470, y=100)

cname = tk.Label(windo, text="Zhejiang University", width=15, height=1, fg="white", bg="lime green", font=('times', 19, ' bold '))
cname.place(x=470, y=150)

field = tk.Label(windo, text="Field", width=9, height=1, fg="white", bg="blue2", font=('times', 19, ' bold '))
field.place(x=305, y=200)

fn = tk.Label(windo, text="Computer Science", width=15, height=1, fg="white", bg="lime green", font=('times', 19, ' bold '))
fn.place(x=470, y=200)

Enrollment = tk.Label(windo, text="Enrollment", width=9, height=1, fg="white", bg="blue2", font=('times', 19, ' bold '))
Enrollment.place(x=305, y=250)

en = tk.Label(windo, text="L201529100140", width=15, height=1, fg="white", bg="lime green", font=('times', 19, ' bold '))
en.place(x=470, y=250)

dn = tk.Label(windo, text="About Developer", width=15, height=1, fg="white", bg="purple", font=('times', 19, ' bold '))
dn.place(x=390, y=50)

sad_img = ImageTk.PhotoImage(Image.open("C:/Users/kusha/PycharmProjects/GUI Emusic/images/student.png"))
panel4 = Label(windo, image = sad_img)
panel4.pack()
panel4.place(x = 30,y=50)

logo = ImageTk.PhotoImage(Image.open("C:/Users/kusha/PycharmProjects/GUI Emusic/images/logo.png"))
panel5 = Label(windo, image = logo)
panel5.pack()
panel5.place(x = 400,y=290)

windo.mainloop()