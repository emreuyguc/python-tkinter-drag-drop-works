from tkinter import *
import time
pnc = Tk()

def yap(ev1):
    mm=ev1
    genislik = mm.widget.winfo_width()#40
    ortax = round(genislik/2)#20
    yukseklik = mm.widget.winfo_height()
    ortay= round(yukseklik/2)
    wx=mm.widget.winfo_rootx()-pnc.winfo_rootx()
    wy=mm.widget.winfo_rooty()-pnc.winfo_rooty()
    yarikontrolx = mm.x_root-mm.widget.winfo_rootx()
    yarikontroly = mm.y_root-mm.widget.winfo_rooty()
    gidilcekx = yarikontrolx-ortax
    gidilceky = yarikontroly-ortay
    mm.widget.place_configure(x=wx+(gidilcekx),y=wy+(gidilceky))


b1 = Button(text="SURUKLEE",bg="red")
b1.place(x=50,y=0)

b1.bind("<B1-Motion>",yap)
pnc.mainloop()
