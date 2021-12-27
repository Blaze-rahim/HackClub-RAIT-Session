import tkinter as tk
import tkinter.messagebox
from tkinter import *

rootie = tk.Tk()

rootie.title("TTT Tkinter")

c = 1

mrcheker = True

boolie = True


def signal(b):
    global c, boolie, mrcheker

    if b["text"] == " " and c == 1:
        b["text"] = "X"
        c = 0

    elif b["text"] == " " and c == 0:
        b["text"] = "O"
        c = 1

    for i in range(10):

        if b1["text"] == "X":
            b1["bg"] = "red"
            b1["fg"] = "black"

        if b2["text"] == "X":
            b2["bg"] = "red"
            b2["fg"] = "black"

        if b3["text"] == "X":
            b3["bg"] = "red"
            b3["fg"] = "black"

        if b4["text"] == "X":
            b4["bg"] = "red"
            b4["fg"] = "black"

        if b5["text"] == "X":
            b5["bg"] = "red"
            b5["fg"] = "black"

        if b6["text"] == "X":
            b6["bg"] = "red"
            b6["fg"] = "black"

        if b7["text"] == "X":
            b7["bg"] = "red"
            b7["fg"] = "black"

        if b8["text"] == "X":
            b8["bg"] = "red"
            b8["fg"] = "black"

        if b9["text"] == "X":
            b9["bg"] = "red"
            b9["fg"] = "black"

        #For O
        if b1["text"] == "O":
            b1["bg"] = "yellow"
            b1["fg"] = "purple"

        if b2["text"] == "O":
            b2["bg"] = "yellow"
            b2["fg"] = "purple"

        if b3["text"] == "O":
            b3["bg"] = "yellow"
            b3["fg"] = "purple"

        if b4["text"] == "O":
            b4["bg"] = "yellow"
            b4["fg"] = "purple"

        if b5["text"] == "O":
            b5["bg"] = "yellow"
            b5["fg"] = "purple"

        if b6["text"] == "O":
            b6["bg"] = "yellow"
            b6["fg"] = "purple"

        if b7["text"] == "O":
            b7["bg"] = "yellow"
            b7["fg"] = "purple"

        if b8["text"] == "O":
            b8["bg"] = "yellow"
            b8["fg"] = "purple"

        if b9["text"] == "O":
            b9["bg"] = "yellow"
            b9["fg"] = "purple"

        if b1["text"] == b2["text"] == b3["text"] != " ":

            if b1['text'] == "X" and mrcheker is True:

                b1["bg"] = "green"
                b2["bg"] = "green"
                b3["bg"] = "green"
                frame["bg"] = "magenta"
                plyr = "Player_1"
                tkinter.messagebox.showinfo(f"Winner is {plyr}", "finally X  won!!!!!!!!!!!!!!!!!!!!")

                z = int(playerX.get())
                scre = z + 1
                playerX.set(scre)

                mrcheker = False

            elif b1['text'] == "O" and mrcheker is True:

                b1["bg"] = "green"
                b2["bg"] = "green"
                b3["bg"] = "green"
                frame["bg"] = "magenta"
                plyr = "Player_2"
                tkinter.messagebox.showinfo(f"Winner is {plyr}", "finally O  won!!!!!!!!!!!!!!!!!!!!")

                z = int(playerY.get())
                scre = z + 1
                playerY.set(scre)

                mrcheker = False

            break

        elif b4["text"] == b5["text"] == b6["text"] != " ":

            if b4['text'] == "X" and mrcheker is True:

                b4["bg"] = "green"
                b5["bg"] = "green"
                b6["bg"] = "green"
                frame["bg"] = "magenta"
                plyr = "Player_1"
                tkinter.messagebox.showinfo(f"Winner is {plyr}", "finally X  won!!!!!!!!!!!!!!!!!!!!")

                z = int(playerX.get())
                scre = z + 1
                playerX.set(scre)
                mrcheker = False

            elif b4['text'] == "O" and mrcheker is True:

                b4["bg"] = "green"
                b5["bg"] = "green"
                b6["bg"] = "green"
                frame["bg"] = "magenta"
                plyr = "Player_2"
                tkinter.messagebox.showinfo(f"Winner is {plyr}", "finally O  won!!!!!!!!!!!!!!!!!!!!")

                z = int(playerY.get())
                scre = z + 1
                playerY.set(scre)

                mrcheker = False
            break

        elif b7["text"] == b8["text"] == b9["text"] != " ":

            if b7['text'] == "X" and mrcheker is True:

                b7["bg"] = "green"
                b8["bg"] = "green"
                b9["bg"] = "green"
                frame["bg"] = "magenta"
                plyr = "Player_1"
                tkinter.messagebox.showinfo(f"Winner is {plyr}", "finally X  won!!!!!!!!!!!!!!!!!!!!")

                z = int(playerX.get())
                scre = z + 1
                playerX.set(scre)

                mrcheker = False

            elif b7['text'] == "O" and mrcheker is True:

                b7["bg"] = "green"
                b8["bg"] = "green"
                b9["bg"] = "green"
                frame["bg"] = "magenta"
                plyr = "Player_2"
                tkinter.messagebox.showinfo(f"Winner is {plyr}", "finally O  won!!!!!!!!!!!!!!!!!!!!")

                z = int(playerY.get())
                scre = z + 1
                playerY.set(scre)

                mrcheker = False

            break

        elif b7["text"] == b4["text"] == b1["text"] != " ":

            if b7['text'] == "X" and mrcheker is True:

                b7["bg"] = "green"
                b4["bg"] = "green"
                b1["bg"] = "green"
                frame["bg"] = "magenta"
                plyr = "Player_1"
                tkinter.messagebox.showinfo(f"Winner is {plyr}", "finally X  won!!!!!!!!!!!!!!!!!!!!")

                z = int(playerX.get())
                scre = z + 1
                playerX.set(scre)

                mrcheker = False

            elif b7['text'] == "O" and mrcheker is True:

                b7["bg"] = "green"
                b4["bg"] = "green"
                b1["bg"] = "green"
                frame["bg"] = "magenta"
                plyr = "Player_2"
                tkinter.messagebox.showinfo(f"Winner is {plyr}", "finally O  won!!!!!!!!!!!!!!!!!!!!")

                z = int(playerY.get())
                scre = z + 1
                playerY.set(scre)
                mrcheker = False
            break

        elif b2["text"] == b5["text"] == b8["text"] != " ":
            if b2['text'] == "X" and mrcheker is True:

                b2["bg"] = "green"
                b5["bg"] = "green"
                b8["bg"] = "green"
                frame["bg"] = "magenta"
                plyr = "Player_1"
                tkinter.messagebox.showinfo(f"Winner is {plyr}", "finally X  won!!!!!!!!!!!!!!!!!!!!")

                z = int(playerX.get())
                scre = z + 1
                playerX.set(scre)
                mrcheker = False

            elif b2['text'] == "O" and mrcheker is True:

                b2["bg"] = "green"
                b5["bg"] = "green"
                b8["bg"] = "green"
                frame["bg"] = "magenta"
                plyr = "Player_2"
                tkinter.messagebox.showinfo(f"Winner is {plyr}", "finally O  won!!!!!!!!!!!!!!!!!!!!")

                z = int(playerY.get())
                scre = z + 1
                playerY.set(scre)

                mrcheker = False

            break

        elif b9["text"] == b6["text"] == b3["text"] != " ":

            if b9['text'] == "X" and mrcheker is True:

                b9["bg"] = "green"
                b6["bg"] = "green"
                b3["bg"] = "green"
                frame["bg"] = "magenta"
                plyr = "Player_1"
                tkinter.messagebox.showinfo(f"Winner is {plyr}", "finally X  won!!!!!!!!!!!!!!!!!!!!")

                z = int(playerX.get())
                scre = z + 1
                playerX.set(scre)
                mrcheker = False
            elif b9['text'] == "O" and mrcheker is True:

                b9["bg"] = "green"
                b6["bg"] = "green"
                b3["bg"] = "green"
                frame["bg"] = "magenta"
                plyr = "Player_2"
                tkinter.messagebox.showinfo(f"Winner is {plyr}", "finally O  won!!!!!!!!!!!!!!!!!!!!")

                z = int(playerY.get())
                scre = z + 1
                playerY.set(scre)

                mrcheker = False

            break

        elif b1["text"] == b5["text"] == b9["text"] != " ":

            if b1['text'] == "X" and mrcheker is True:

                b1["bg"] = "green"
                b5["bg"] = "green"
                b9["bg"] = "green"
                frame["bg"] = "magenta"
                plyr = "Player_1"
                tkinter.messagebox.showinfo(f"Winner is {plyr}", "finally X  won!!!!!!!!!!!!!!!!!!!!")

                z = int(playerX.get())
                scre = z + 1
                playerX.set(scre)

                mrcheker = False

            elif b1['text'] == "O" and mrcheker is True:

                b1["bg"] = "green"
                b5["bg"] = "green"
                b9["bg"] = "green"
                frame["bg"] = "magenta"
                plyr = "Player_2"
                tkinter.messagebox.showinfo(f"Winner is {plyr}", "finally O  won!!!!!!!!!!!!!!!!!!!!")

                z = int(playerY.get())
                scre = z + 1
                playerY.set(scre)

                mrcheker = False

            break

        elif b7["text"] == b5["text"] == b3["text"] != " ":

            if b7['text'] == "X" and mrcheker is True:

                b7["bg"] = "green"
                b5["bg"] = "green"
                b3["bg"] = "green"
                frame["bg"] = "magenta"
                plyr = "Player_1"
                tkinter.messagebox.showinfo(f"Winner is {plyr}", "finally X  won!!!!!!!!!!!!!!!!!!!!")

                z = int(playerX.get())
                scre = z + 1
                playerX.set(scre)

                mrcheker = False

            elif b7['text'] == "O" and mrcheker is True:

                b7["bg"] = "green"
                b5["bg"] = "green"
                b3["bg"] = "green"
                frame["bg"] = "magenta"
                plyr = "Player_2"
                tkinter.messagebox.showinfo(f"Winner is {plyr}", "finally O  won!!!!!!!!!!!!!!!!!!!!")

                z = int(playerY.get())
                scre = z + 1
                playerY.set(scre)
                mrcheker = False

            break

        elif (b1['text'] != " " and b2['text'] != " " and b3['text'] != " " and b4['text'] != " " and
              b5['text'] != " " and b6['text'] != " " and b7['text'] != " " and b8['text'] != " " and
              b9['text'] != " "):

            tkinter.messagebox.showinfo("It's a Tie!!", "Well played : ))")

            break


def reset():
    b1["text"] = " "
    b2["text"] = " "
    b3["text"] = " "
    b4["text"] = " "
    b5["text"] = " "
    b6["text"] = " "
    b7["text"] = " "
    b8["text"] = " "
    b9["text"] = " "

    b1["bg"] = "gainsboro"
    b2["bg"] = "gainsboro"
    b3["bg"] = "gainsboro"
    b4["bg"] = "gainsboro"
    b5["bg"] = "gainsboro"
    b6["bg"] = "gainsboro"
    b7["bg"] = "gainsboro"
    b8["bg"] = "gainsboro"
    b9["bg"] = "gainsboro"

    frame["bg"] = "purple"

    global c, mrcheker
    c = 1
    mrcheker = True


def newgame():
    reset()
    playerX.set(0)
    playerY.set(0)


HEIGHT = 700
WIDTH = 70000

canvas = tk.Canvas(rootie, height=HEIGHT, width=WIDTH)
canvas.pack()

filename = PhotoImage(file="C:\\Users\\AbdulRahim\\Downloads\\8.png")
background_label = Label(rootie, image=filename)
background_label.place(x=0, y=5, relwidth=1, relheight=1.2)


frame = tk.Frame(rootie, bg='purple', bd=5)
frame.place(relx=0.28, rely=0.15, relwidth=0.5, relheight=0.8, anchor='n')


frame2 = tk.Frame(rootie, bg='cyan', bd=5)
frame2.place(relx=0.745, rely=0.17, relwidth=0.4, relheight=0.27, anchor='n')


frame3 = tk.Frame(rootie, bg='red', bd=5)
frame3.place(relx=0.74563, rely=0.45, relwidth=0.4, relheight=0.4, anchor='n')


btnreset = tk.Button(frame3, text="Reset", font=('Helvetica', 50), bg="gainsboro", height=3, width=6,
                     command=lambda: reset())
btnreset.place(relx=0.1, rely=0.15, relheight=0.3, relwidth=0.8)


btnnew = tk.Button(frame3, text="New Game", font=('Helvetica', 50), bg="gainsboro", height=3, width=6,
                   command=lambda: newgame())
btnnew.place(relx=0.1, rely=0.55, relheight=0.3, relwidth=0.8)


lab = tk.Label(frame2, text="Player_1 : ", bg="cyan", fg="black", font=('Helvetica', 23))
lab.place(relx=0.03, rely=0.17)


playerX = IntVar()
playerY = IntVar()


playerX.set(0)
playerY.set(0)


p1score = Entry(frame2, textvariable=playerX, fg="black", width=14, font=("Times", 24), justify=LEFT)
p1score.place(relx=0.34, rely=0.18)

p2score = Entry(frame2, textvariable=playerY, fg="black", width=14, font=("Times", 24), justify=LEFT)
p2score.place(relx=0.34, rely=0.58)


lab1 = tk.Label(frame2, text="Player_2 :", bg="cyan", fg="black", font=('Helvetica', 23))
lab1.place(relx=0.03, rely=0.57)


b1 = tk.Button(frame, text=" ", font=('Helvetica', 50), bg="gainsboro", height=3, width=6,
               command=lambda: signal(b1))  # 7
b1.place(relx=0.02, rely=0.037, relheight=0.3, relwidth=0.3)


b2 = tk.Button(frame, text=" ", font=('Helvetica', 50), bg="gainsboro", height=3, width=6,
               command=lambda: signal(b2))  # 8
b2.place(relx=0.345, rely=0.037, relheight=0.3, relwidth=0.3)


b3 = tk.Button(frame, text=" ", font=('Helvetica', 50), bg="gainsboro", height=3, width=6,
               command=lambda: signal(b3))  # 9
b3.place(relx=0.67, rely=0.037, relheight=0.3, relwidth=0.3)


b4 = tk.Button(frame, text=" ", font=('Helvetica', 50), bg="gainsboro", height=3, width=6,
               command=lambda: signal(b4))  # 4
b4.place(relx=0.02, rely=0.35, relheight=0.3, relwidth=0.3)


b5 = tk.Button(frame, text=" ", font=('Helvetica', 50), bg="gainsboro", height=3, width=6,
               command=lambda: signal(b5))  # 5
b5.place(relx=0.345, rely=0.35, relheight=0.3, relwidth=0.3)


b6 = tk.Button(frame, text=" ", font=('Helvetica', 50), bg="gainsboro", height=3, width=6,
               command=lambda: signal(b6))  # 6
b6.place(relx=0.67, rely=0.35, relheight=0.3, relwidth=0.3)


b7 = tk.Button(frame, text=" ", font=('Helvetica', 50), bg="gainsboro", height=3, width=6,
               command=lambda: signal(b7))  # 1
b7.place(relx=0.02, rely=0.66, relheight=0.3, relwidth=0.3)


b8 = tk.Button(frame, text=" ", font=('Helvetica', 50), bg="gainsboro", height=3, width=6,
               command=lambda: signal(b8))  # 2
b8.place(relx=0.345, rely=0.66, relheight=0.3, relwidth=0.3)


b9 = tk.Button(frame, text=" ", font=('Helvetica', 50), bg="gainsboro", height=3, width=6,
               command=lambda: signal(b9))  # 3
b9.place(relx=0.67, rely=0.66, relheight=0.3, relwidth=0.3)


tk.mainloop()
