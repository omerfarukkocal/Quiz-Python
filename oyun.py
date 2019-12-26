from tkinter import *
import tkinter.messagebox as tkm
import giris
import sqlite3

global score
score = 0

global i
i = 0


def siralamayaEkle():

    cursor.execute("INSERT INTO eniyiler VALUES(?,?)",(score,giris.nick))
    con.commit()


def siradakiSoru():

    global i

    if (i>=10):
        l1["text"] = "OYUN BİTTİ"
        l1.pack()
        e1["font"] = "Verdana 28"
        e1.pack()
        e3["text"] = "SKORUNUZ: " + str(score)
        e3.pack()
        e3["font"] = "Verdana 28"
        e2.destroy()
        b1.destroy()
        b2.destroy()
        b3.destroy()
        b4.destroy()

        siralamayaEkle()

    else:
        l1["text"] = str(i+1)+". SORU"
        l1.pack()

        e2["text"] = data[i][0]
        e2.pack()

        b1["text"] = "A) "+data[i][1]
        b1.pack()
        b2["text"] = "B) "+data[i][2]
        b2.pack()
        b3["text"] = "C) "+data[i][3]
        b3.pack()
        b4["text"] = "D) "+data[i][4]
        b4.pack()
        e3["text"] = "Skorunuz: "+str(score)
        e3.pack()


def a():
    cevap("a")

def b():
    cevap("b")

def c():
    cevap("c")

def d():
    cevap("d")

def cevap(x):
    global i
    global score
    if data[i][5] == x:
        score += 10
        tkm.showinfo("","DOĞRU CEVAP")
    else:
        tkm.showwarning("","YANLIŞ CEVAP")

    i += 1
    siradakiSoru()



def oyun():

    global i
    global score
    global con
    global cursor
    con = sqlite3.connect("veritabani")
    cursor = con.cursor()

    cursor.execute("SELECT * FROM sorular")
    global data
    data = cursor.fetchall()

    p = Toplevel()
    p.geometry("1200x800+100+200")
    p.title("Bilgi Yarışması")

    global l1
    l1 = Label(p,text=str(i+1)+". SORU", font="Verdana 30", fg="Gray")
    l1.pack()

    global e1
    e1 = Label(p,text=giris.nick, font="Verdana 18", fg="Red")
    e1.pack()

    global e2
    e2 = Label(p,text=data[i][0], font="Verdana 18", fg="Green")
    e2.pack()

    global b1
    global b2
    global b3
    global b4
    b1 = Button(p,text="A) " + data[i][1], font="Verdana 15", command=a)
    b1.pack()
    b2 = Button(p,text="B) " + data[i][2], font="Verdana 15", command=b)
    b2.pack()
    b3 = Button(p,text="C) " + data[i][3], font="Verdana 15", command=c)
    b3.pack()
    b4 = Button(p,text="D) " + data[i][4], font="Verdana 15", command=d)
    b4.pack()

    global e3
    e3 = Label(p,text="Skorunuz: " + str(score), font="Verdana 12", fg="blue")
    e3.pack()






    p.mainloop()

