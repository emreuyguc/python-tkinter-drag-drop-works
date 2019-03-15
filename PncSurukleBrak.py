from tkinter import *
import time

Pencere = Tk()

def SurukleBirak(Olay):
    Fare=Olay
    Eleman = b1
    ElemanGenisligi = Eleman.winfo_width()
    ElemanYuksekligi = Eleman.winfo_height()
    OrtaX = round(ElemanGenisligi/2)
    OrtaY= round(ElemanYuksekligi/2)
    ElemanX=Eleman.winfo_rootx()-Pencere.winfo_rootx()
    ElemanY=Eleman.winfo_rooty()-Pencere.winfo_rooty()
    FareYariKontrolX = Fare.x_root-Eleman.winfo_rootx()
    FareYariKontrolY = Fare.y_root-Eleman.winfo_rooty()
    if FareYariKontrolX>1 and FareYariKontrolX<ElemanGenisligi-1:
        if FareYariKontrolY>1 and FareYariKontrolY<ElemanYuksekligi-1:
            GidilcekX = FareYariKontrolX-OrtaX
            GidilcekY = FareYariKontrolY-OrtaY
            b1.place_configure(x=ElemanX+(GidilcekX),y=ElemanY+(GidilcekY))
    

b1 = Button(text="SURUKLEE",bg="red",width=5,height=5)
l1 = Listbox(bg="red")
c1 = Checkbutton()
b1.place(x=50,y=0)

Pencere.bind("<B1-Motion>",SurukleBirak)

Pencere.mainloop()
