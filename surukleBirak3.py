from tkinter import *
import time

Pencere = Tk()

def ilk(e):
    global basx,basy
    mm=e
    basx=mm.x
    basy=mm.y
        
def iki(e):
    global basx,basy
    mm=e
    x= b1.winfo_x()-basx+e.x
    y= b1.winfo_y()-basy+e.y
    b1.place(x=x,y=y)

def son(e):
    Pencere.unbind("<Leave>")
    
b1 = Button(text="SURUKLEE",bg="red")
l1 = Listbox(bg="red")
c1 = Checkbutton()
b1.place(x=50,y=0)

b1.bind("<1>",ilk)
b1.bind("<B1-Motion>",iki)
b1.bind("<ButtonRelease-1>",son)
Pencere.mainloop()
