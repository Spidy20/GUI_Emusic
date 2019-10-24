import tkinter as tk
from tkinter import *
import cv2
import csv
import os
import numpy as np
from PIL import Image,ImageTk
import pandas as pd
import datetime
import time
from PIL import ImageTk, Image
import pygame

#####Window is our Main frame of system

window = tk.Tk()
window.title("EMUSIC - An Emo;tion Base Music Player")

message = tk.Label(window, text="EMUSIC - An Emotion Base Music Player", bg="black", fg="white", width=50,
                   height=3, font=('times', 30, 'italic bold '))

message.place(x=80, y=20)

global status

status = tk.Label(window, text="You looking a Happy ,Playing Happy playlist fot you:)", bg="limegreen", fg="black", width=45,
                   height=1, font=('times', 25, 'italic bold '))

def about_me():
    windo = Toplevel()
    windo.iconbitmap('C:/Users/kusha/PycharmProjects/GUI Emusic/icons/music.ico')
    windo.title("About Me")
    windo.geometry('820x420')
    windo.resizable(0, 0)
    sub = tk.Label(windo, text="Name", width=9, height=1, fg="white", bg="blue2", font=('times', 19, ' bold '))
    sub.place(x=305, y=100)
    col = tk.Label(windo, text="College", width=9, height=1, fg="white", bg="blue2", font=('times', 19, ' bold '))
    col.place(x=305, y=150)
    dname = tk.Label(windo, text="Bhavsar Kushal", width=15, height=1, fg="white", bg="lime green",
                     font=('times', 19, ' bold '))
    dname.place(x=470, y=100)
    cname = tk.Label(windo, text="GANPAT University", width=15, height=1, fg="white", bg="lime green",
                     font=('times', 19, ' bold '))
    cname.place(x=470, y=150)
    field = tk.Label(windo, text="Field", width=9, height=1, fg="white", bg="blue2", font=('times', 19, ' bold '))
    field.place(x=305, y=200)
    fn = tk.Label(windo, text="IT", width=15, height=1, fg="white", bg="lime green",
                  font=('times', 19, ' bold '))
    fn.place(x=470, y=200)
    Enrollment = tk.Label(windo, text="Enrollment", width=9, height=1, fg="white", bg="blue2",
                          font=('times', 19, ' bold '))
    Enrollment.place(x=305, y=250)
    en = tk.Label(windo, text="19012022001", width=15, height=1, fg="white", bg="lime green",
                  font=('times', 19, ' bold '))
    en.place(x=470, y=250)
    dn = tk.Label(windo, text="About Developer", width=15, height=1, fg="white", bg="purple",
                  font=('times', 19, ' bold '))
    dn.place(x=390, y=50)
    sad_img = ImageTk.PhotoImage(Image.open("C:/Users/kusha/PycharmProjects/GUI Emusic/images/student.png"))
    panel4 = Label(windo, image=sad_img)
    panel4.pack()
    panel4.place(x=30, y=50)
    # logo = ImageTk.PhotoImage(Image.open("C:/Users/kusha/PycharmProjects/GUI Emusic/images/logo.png"))
    # panel5 = Label(windo, image=logo)
    # panel5.pack()
    # panel5.place(x=400, y=290)
    windo.mainloop()

def emotion_music():
    # From:- Techmicra IT solution
    import time
    import cv2
    import label_image
    import os, random
    import subprocess
    os.environ["OPENCV_VIDEOIO_PRIORITY_MSMF"] = "0"

    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

    def playsong(directory):
        import os
        from tkinter.filedialog import askdirectory
        import pygame
        from mutagen.id3 import ID3
        from ttkthemes import themed_tk as tk

        root = tk.ThemedTk()
        root.get_themes()  # Returns a list of all themes that can be set
        root.set_theme("radiance")
        root.title('MUSIC PLAYER')
        root.minsize(500, 500)
        root.iconbitmap('C:/Users/kusha/PycharmProjects/GUI Emusic/icons/music.ico')
        root.resizable(0, 0)

        listbox = Listbox(root, selectmode=SINGLE, width=100, height=20, bg="#0ff", fg="black")
        listbox.pack(fill=X)

        sb = Scrollbar(root, orient='vertical')
        sb.configure(command=listbox.yview)
        sb.pack(side="right", fill="y")

        listbox.configure(yscrollcommand=sb.set)

        listofsongs = []
        realnames = []

        v = StringVar()
        songlabel = Label(root, textvariable=v, width=80)
        global index,count,ctr
        index = 0
        count = 0
        ctr = 0

        if directory == 'C:/Users/kusha/PycharmProjects/Music_player_with_Emotions_recognition/songs/Angry/':
            root.title('Angry Playlist')

        if directory == 'C:/Users/kusha/PycharmProjects/Music_player_with_Emotions_recognition/songs/Smile/':
            root.title('Happy Playlist')

        if directory == 'C:/Users/kusha/PycharmProjects/Music_player_with_Emotions_recognition/songs/Fear/':
            root.title('Fear Playlist')

        if directory == 'C:/Users/kusha/PycharmProjects/Music_player_with_Emotions_recognition/songs/Sad/':
            root.title('Sad Playlist')

        def updatelabel():
            global index
            global songname
            v.set(listofsongs[index])
            # return songname

        def pausesong(event):
            global ctr
            ctr += 1
            if (ctr % 2 != 0):
                pygame.mixer.music.pause()
                statusbar['text'] = "Music Pause"
            if (ctr % 2 == 0):
                pygame.mixer.music.unpause()
                statusbar['text'] = "Playing music" + ' - ' + os.path.basename(listofsongs[index])

        def playsong(event):
            pygame.mixer.music.play()

        def nextsong(event):
            global index
            index += 1
            if (index < count):
                pygame.mixer.music.load(listofsongs[index])
                pygame.mixer.music.play()
                statusbar['text'] = "Playing music" + ' - ' + os.path.basename(listofsongs[index])
                audio = MP3(listofsongs[index])
                x = audio.info.length
                mins, secs = divmod(x, 60)
                mins = round(mins)
                secs = round(secs)
                timeformat2 = '{:02d}:{:02d}'.format(mins, secs)
                length['text'] = "Total Length" + ' - ' + timeformat2
                listbox.itemconfig(index, bg='pink')
            else:
                index = 0
                pygame.mixer.music.load(listofsongs[index])
                statusbar['text'] = "Playing music" + ' : ' + os.path.basename(listofsongs[index])
                pygame.mixer.music.play()
                listbox.itemconfig(index, bg='pink')
                # listbox.selection_set(first=index)
            try:
                updatelabel()
            except NameError:
                print("")

        def previoussong(event):
            global index
            index -= 1
            pygame.mixer.music.load(listofsongs[index])
            statusbar['text'] = "Playing music" + ' - ' + os.path.basename(listofsongs[index])

            audio = MP3(listofsongs[index])
            x = audio.info.length
            mins, secs = divmod(x, 60)
            mins = round(mins)
            secs = round(secs)
            timeformat1 = '{:02d}:{:02d}'.format(mins, secs)
            length['text'] = "Total Length" + ' - ' + timeformat1
            pygame.mixer.music.play()
            listbox.itemconfig(index, bg='pink')
            # listbox.selection_set(first=index)
            try:
                updatelabel()
            except NameError:
                print("")

        os.chdir(directory)
        for files in os.listdir(directory):
            try:
                if files.endswith(".mp3"):
                    realdir = os.path.realpath(files)
                    audio = ID3(realdir)
                    realnames.append(audio['TIT2'].text[0])
                    listofsongs.append(files)
            except:
                print(files + " is not a song")

        listbox.delete(0, END)
        realnames.reverse()
        for items in realnames:
            listbox.insert(0, items)
        for i in listofsongs:
            count = count + 1
        pygame.mixer.init()
        pygame.mixer.music.load(listofsongs[index])
        pygame.mixer.music.play()
        listbox.itemconfig(index, bg='pink')

        from mutagen.mp3 import MP3
        audio = MP3(listofsongs[index])
        x = audio.info.length
        print(x)
        mins, secs = divmod(x, 60)
        mins = round(mins)
        secs = round(secs)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)

        def del_music(self):
            items = map(int, listbox.curselection())
            for item in items:
                listbox.delete(item)
                listofsongs.pop(item)
                print(listofsongs)

        def play_music(self):
            items = map(int, listbox.curselection())
            for item in items:
                item = int(item)
                pygame.mixer.music.load(listofsongs[item])
                statusbar['text'] = "Playing music" + ' - ' + os.path.basename(listofsongs[item])
                audio = MP3(listofsongs[item])
                x = audio.info.length
                mins, secs = divmod(x, 60)
                mins = round(mins)
                secs = round(secs)
                timeformat1 = '{:02d}:{:02d}'.format(mins, secs)
                length['text'] = "Total Length" + ' - ' + timeformat1
                pygame.mixer.music.play()
                listbox.itemconfig(item, bg='pink')

        def add_music(self):
            import tkinter as tk
            from tkinter import filedialog
            rt = tk.Tk()
            rt.withdraw()
            global filename
            filename = filedialog.askopenfilename()
            print(filename)
            listofsongs.insert(index, filename)
            # listofsongs.append(filename)
            print(listofsongs)
            listbox.insert(index, filename)

            rt.mainloop()

        def show_value(self):
            i = vol.get()
            pygame.mixer.music.set_volume(i)

        length = Label(root, text="Welcome to Melody", font='Times 13 bold')
        length.pack(side=BOTTOM, fill=X)
        length.place(x=10, y=445)
        length['text'] = "Total Length" + ' - ' + timeformat

        def mute(self):
            vol.set(0)
            if vol.set(0):
                vol.set(10)

        def on_closing():
            from tkinter import messagebox
            if messagebox.askokcancel("Quit", "Do you want to quit?"):
                pygame.mixer.music.stop()
                global window
                window.destroy()
                root.destroy()

        root.protocol("WM_DELETE_WINDOW", on_closing)

        vol = Scale(root, from_=0, to=10, orient=HORIZONTAL, resolution=10, command=show_value)
        vol.place(x=910, y=436)
        vol.set(10)

        volume = Label(root, text="Volume", font='Times 13 bold')
        volume.place(x=840, y=450)

        statusbar = Label(root, text="Welcome to Melody", relief=SUNKEN, anchor=W, background='lime green',
                          font='Times 13 bold italic')
        statusbar.pack(side=BOTTOM, fill=X)

        statusbar['text'] = "Playing Music" + ' - ' + os.path.basename(listofsongs[index])

        framemiddle = Frame(root, width=250, height=30)
        framemiddle.pack()

        framedown = Frame(root, width=400, height=300)
        framedown.pack()

        previousbutton = Button(framedown, text="◄◄", bg='#0ff', activebackground="Red", width=15, height=2)
        previousbutton.pack(side=LEFT)

        playbutton = Button(framedown, text="►", activebackground="Red", width=15, height=2)
        playbutton.pack(side=LEFT)

        mutebtn = Button(framedown, text="Play", activebackground="Red", width=15, height=2)
        mutebtn.pack(side=LEFT)

        pausebutton = Button(framedown, bg='red', text="►/║║", activebackground="white", width=15, height=2)
        pausebutton.pack(side=LEFT)

        del_button = Button(framedown, text="Del Song", activebackground="Red", width=15, height=2)
        del_button.pack(side=LEFT)

        add_button = Button(framedown, text="Add Song", activebackground="Red", width=15, height=2)
        add_button.pack(side=LEFT)

        nextbutton = Button(framedown, text="►►", bg='#0ff', activebackground="Red", width=15, height=2)
        nextbutton.pack(side=LEFT)

        playbutton.bind("<Button-1>", playsong)
        nextbutton.bind("<Button-1>", nextsong)
        previousbutton.bind("<Button-1>", previoussong)
        mutebtn.bind("<Button-1>", play_music)
        pausebutton.bind("<Button-1>", pausesong)
        del_button.bind("<Button-1>", del_music)
        add_button.bind("<Button-1>", add_music)
        root.mainloop()

    size = 4
    # We load the xml file
    classifier = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
    global text
    webcam = cv2.VideoCapture(0)  # Using default WebCam connected to the PC.
    now = time.time()  ###For calculate seconds of videos
    future = now + 13  ####here is second of time which taken by emotion recognition system ,you can change it
    while True:
        (rval, im) = webcam.read()
        im = cv2.flip(im, 1, 0)  # Flip to act as a mirror
        # Resize the image to speed up detection
        mini = cv2.resize(im, (int(im.shape[1] / size), int(im.shape[0] / size)))
        # detect MultiScale / faces
        faces = classifier.detectMultiScale(mini)
        # Draw rectangles around each face
        for f in faces:
            (x, y, w, h) = [v * size for v in f]  # Scale the shapesize backup
            sub_face = im[y:y + h, x:x + w]
            FaceFileName = "test.jpg"  # Saving the current image from the webcam for testing.
            cv2.imwrite(FaceFileName, sub_face)
            text = label_image.main(
                FaceFileName)  # Getting the Result from the label_image file, i.e., Classification Result.
            text = text.title()  # Title Case looks Stunning.
            font = cv2.FONT_HERSHEY_TRIPLEX

            if text == 'Angry':
                cv2.rectangle(im, (x, y), (x + w, y + h), (0, 25, 255), 7)
                cv2.putText(im, text, (x + h, y), font, 1, (0, 25, 255), 2)

            if text == 'Smile':
                cv2.rectangle(im, (x, y), (x + w, y + h), (0, 260, 0), 7)
                cv2.putText(im, text, (x + h, y), font, 1, (0, 260, 0), 2)

            if text == 'Fear':
                cv2.rectangle(im, (x, y), (x + w, y + h), (0, 255, 255), 7)
                cv2.putText(im, text, (x + h, y), font, 1, (0, 255, 255), 2)

            if text == 'Sad':
                cv2.rectangle(im, (x, y), (x + w, y + h), (0, 191, 255), 7)
                cv2.putText(im, text, (x + h, y), font, 1, (0, 191, 255), 2)

        # Show the image/
        cv2.imshow('Scanning your Face', im)
        key = cv2.waitKey(30) & 0xff
        if time.time() > future:  ##after 20 second music will play
            try:
                cv2.destroyAllWindows()

                if text == 'Angry':
                    t = 'You Looking Angry, I playing Angry playlist for you:)'
                    status.configure(text = t,bg='Olive Drab1')
                    status.place(x=200, y=585)
                    dc = ("C:/Users/kusha/PycharmProjects/Music_player_with_Emotions_recognition/songs/Angry/")
                    playsong(dc)
                    break

                if text == 'Smile':
                    t = 'You Looking Happy, Playing Happy playlist for you:)'
                    status.configure(text=t, bg='purple1',foreground = 'white')
                    status.place(x=200, y=585)
                    dc = ('C:/Users/kusha/PycharmProjects/Music_player_with_Emotions_recognition/songs/Smile/' )
                    playsong(dc)
                    break

                if text == 'Fear':
                    t = 'You looking scared, wait i Playing fear playlist for you:)'
                    status.configure(text=t, bg='lime green')
                    status.place(x=200, y=585)
                    dc = ("C:/Users/kusha/PycharmProjects/Music_player_with_Emotions_recognition/songs/Fear/")
                    playsong(dc)
                    break
                if text == 'Sad':
                    t = "Don't be Sad,I Playing Sad playlist for you:)"
                    status.configure(text=t, bg='yellow')
                    status.place(x=200, y=585)
                    dc = ("C:/Users/kusha/PycharmProjects/Music_player_with_Emotions_recognition/songs/Sad/")
                    playsong(dc)
                break


            except Exception as e:
                print(e)
                t = "Stay Focus in camera atleast 15 Seconds"
                status.configure(text=t, bg='black',foreground ='white')
                status.place(x=200, y=585)
                cv2.destroyAllWindows()


        if key == 27:  # The Esc key
            cv2.destroyAllWindows()
            break
        k = future+2
        if time.time() > k:
            cv2.destroyAllWindows()
            break


window.iconbitmap('C:/Users/kusha/PycharmProjects/GUI Emusic/icons/music.ico')
window.geometry('1280x720')
window.state('zoomed')

from PIL import ImageTk,Image
face_img = ImageTk.PhotoImage(Image.open("C:/Users/kusha/PycharmProjects/GUI Emusic/images/face-scanner.png"))
panel = Label(window, image = face_img)
panel.pack()
panel.place(x = 80,y=200)

music_img = ImageTk.PhotoImage(Image.open("C:/Users/kusha/PycharmProjects/GUI Emusic/images/music-player.png"))
panel = Label(window, image = music_img)
panel.pack()
panel.place(x = 980,y=200)

smile_img = ImageTk.PhotoImage(Image.open("C:/Users/kusha/PycharmProjects/GUI Emusic/images/smile.png"))
panel1 = Label(window, image = smile_img)
panel1.pack()
panel1.place(x = 455,y=280)

angry_img = ImageTk.PhotoImage(Image.open("C:/Users/kusha/PycharmProjects/GUI Emusic/images/angry.png"))
panel2 = Label(window, image = angry_img)
panel2.pack()
panel2.place(x = 785,y=280)

scare_img = ImageTk.PhotoImage(Image.open("C:/Users/kusha/PycharmProjects/GUI Emusic/images/ff.png"))
panel3 = Label(window, image = scare_img)
panel3.pack()
panel3.place(x = 455,y=450)

sad_img = ImageTk.PhotoImage(Image.open("C:/Users/kusha/PycharmProjects/GUI Emusic/images/sad.png"))
panel4 = Label(window, image = sad_img)
panel4.pack()
panel4.place(x = 785,y=450)

def on_closing():
    from tkinter import messagebox
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        window.destroy()
        # cv2.destroyAllWindows()
window.protocol("WM_DELETE_WINDOW", on_closing)

play_music = tk.Button(window, text="Play Music",fg="white",command = emotion_music  ,bg="blue2"  ,width=18  ,height=2, activebackground = "Red" ,font=('times', 18, 'bold '))
play_music.place(x=80, y=500)

About = tk.Button(window, text="About Me",fg="white"  ,bg="blue2",command = about_me,width=18  ,height=2, activebackground = "Red" ,font=('times', 18, ' bold '))
About.place(x=990, y=500)

sp_em = tk.Label(window, text="Supported Emotions", width=30, fg="black", bg="deep pink", height=2, font=('times', 20, ' bold '))
sp_em.place(x=445, y=200)

window.geometry('1280x720')

window.mainloop()