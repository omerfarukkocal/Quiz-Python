from tkinter import *
import giris
import tkinter.messagebox as tkm
import oyun

pencere = Tk()
pencere.geometry("800x600+200+100")
pencere.title("Kim Soruları Doğru Cevaplamak İster?")

etiket = Label(text="BİLGİ YARIŞMASI", font="Verdana 40", fg="Gray")
etiket.pack()

etiket2 = Label(text=""+giris.nick, font="Verdana 28", fg="Red")
etiket2.pack()

buton1 = Button(text="En İyiler", font="Verdana",  command=giris.siralama)
buton1.pack(side="left", expand=1)

buton2 = Button(text="Oyuna Başla", font="Verdana", command = oyun.oyun)
buton2.pack(side="left", expand=1)

buton3 = Button(text="Kapat", font="Verdana", command = pencere.destroy)
buton3.pack(side="left", expand=1)

#tkm.showinfo("Uyarı", ""+giris.nick+", oyuna hazırsın.")


pencere.mainloop()