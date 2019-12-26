from tkinter import *
import sqlite3


def nickAl():
    global nick
    nick = text.get()
    pencere.destroy()


pencere = Tk()
pencere.geometry("800x600+200+100")
pencere.title("Bilgi Yarışması")
etiket = Label(text = "\n\nBilgi Yarışmasına hoşgeldiniz.\n\n"
                      "Yarışmayı baştan sona hazırlayan: Ömer Faruk Koçal\n\n"
                      "Aşağıdaki boşluğa kullanıcı adınızı girip oyuna başlayabilirsiniz.\n\n"
                      "Başarılar.\n\n")
etiket["font"] = "Verdana"
etiket.pack()

text = Entry()
text.pack()

dugme = Button(text = "İleri", font="Verdana", command = nickAl)
dugme.pack()

pencere.mainloop()


def oyun():
    zet = Tk()
    zet.title("Oyuna başla")
    zet.geometry("300x300+200+100")
    zet.mainloop()



def siralama():
    ps = Tk()
    ps.title("Sıralama")
    ps.geometry("240x360")


    con = sqlite3.connect("veritabani")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM eniyiler")
    data = cursor.fetchall()
    data.sort()

    plbl = Label(ps,text=data)
    plbl.pack()

    ps.mainloop()





