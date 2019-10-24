from tkinter import *

root = Tk()

root.title('Test frame')
root.configure(background = 'snow')
root.iconbitmap('C:/Users/kusha/PycharmProjects/GUI Emusic/icons/music.ico')
root.state('zoomed')
root.geometry('1280x720')

# def on_closing():
#     from tkinter import messagebox
#     if messagebox.askokcancel("Quit", "Do you want to quit?"):
#         root.destroy()
#         # cv2.destroyAllWindows()
# root.protocol("WM_DELETE_WINDOW", on_closing)
#
def submit():
    wind = Tk()
    wind.title('frame2')
    wind.configure(background = 'limegreen')
    wind.geometry('840x420')
    wind.resizable(0,0)
    wind.iconbitmap('C:/Users/kusha/PycharmProjects/GUI Emusic/icons/music.ico')

    e1 = entry1.get()
    e2 = entry2.get()

    lbl1 = Label(wind, text=e1, width=15, fg='blue', bg='yellow', height=3, font=('times', 15, 'bold '))
    lbl1.place(x=100, y=100)

    lbl2 = Label(wind, text=e2, width=15, fg='blue', bg='yellow', height=3, font=('times', 15, 'bold '))
    lbl2.place(x=100, y=250)

    wind.mainloop()
#
#
lbl1 = Label(root,text = 'Enter name',width = 15,fg = 'blue',bg ='yellow',height = 3,font=('times', 15, 'bold  italic'))
lbl1.place(x = 100, y =100)

lbl2 = Label(root,text = 'Enter surname',width = 15,fg = 'blue',bg ='yellow',height = 3,font=('times', 15, 'bold '))
lbl2.place(x = 100, y =250)

entry1 = Entry(root,width = 22,fg = 'red', bg = 'yellow',font=('times', 25, 'bold '))
entry1.place(x = 300 , y =120)

entry2 = Entry(root,width = 22,fg = 'red', bg = 'yellow',font=('times', 25, 'bold '))
entry2.place(x = 300 , y =270)

btn1 = Button(root,text = 'Submit',command = submit,width =18,fg = 'black',bg = 'lime green',activebackground = 'yellow',font=('times', 25, 'bold ') )
btn1.place(x = 300,y = 470)

root.mainloop()

# # root.geometry('1280x720')
# root.state('zoomed')
#
# lbl2 = Label(root, text="Enter Name", width=15, fg="black", bg="deep pink", height=2, font=('times', 15, ' bold '))
# lbl2.place(x=100, y=300)
#
# lbl3 = Label(root, text="Enter age", width=15, fg="black", bg="deep pink", height=2, font=('times', 15, ' bold '))
# lbl3.place(x=100, y=380)
#
#
# txt2 = Entry(root, width=20, bg="yellow", fg="red", font=('times', 25, ' bold '))
# txt2.place(x=450, y=310)
#
# txt3 = Entry(root, width=20, bg="yellow", fg="red", font=('times', 25, ' bold '))
# txt3.place(x=450, y=380)
#
#

#
#
# takeImg = Button(root, text="Take Images",fg="white"  ,bg="blue2"  ,width=20  ,height=3, activebackground = "Red" ,font=('times', 15, ' bold '))
# takeImg.place(x=450, y=500)
#
# root.mainloop()