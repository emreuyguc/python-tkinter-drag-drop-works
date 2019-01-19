from tkinter import *
import time

Pencere = Tk()

def ilk(e):
    global basx,basy
    mm=e
    if mm.x_root-b1.winfo_rootx()>0 and mm.x<b1.winfo_width():
        basx=mm.x
        basy=mm.y
        
def iki(e):
    global basx,basy
    mm=e
    if mm.x_root-b1.winfo_rootx()>0 and mm.x<b1.winfo_width():
        x= b1.winfo_x()-basx+e.x
        y= b1.winfo_y()-basy+e.y
        b1.place(x=x,y=y)
        Pencere.bind("<Leave>",kacti)

def kacti(e):
    global basx,basy
    x= b1.winfo_x()-basx+e.x
    y= b1.winfo_y()-basy+e.y
    b1.place(x=x,y=y)

def son(e):
    Pencere.unbind("<Leave>")
    
b1 = Button(text="SURUKLEE",bg="red")
l1 = Listbox(bg="red")
c1 = Checkbutton()
b1.place(x=50,y=0)

Pencere.bind("<1>",ilk)
Pencere.bind("<B1-Motion>",iki)
Pencere.bind("<ButtonRelease-1>",son)
Pencere.mainloop()
