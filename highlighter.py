import os
os.system("cls")
from tkinter import *
x1=0
y1=0
def keypress(vchar):
            print(vchar.char)

def painting(position1):
            x=position1.x
            y=position1.y
            c.create_line(x-10,y-10,x+10,y+10,fill="red")

def start(pos):
        global x1,y1
        x1=pos.x
        y1=pos.y

def end(pos):
        global x1,y1
        x2=pos.x
        y2=pos.y
        c.create_line(x1,y1,x2,y2,fill="green")
rt=Tk()
rt.geometry("500x1000")
c=Canvas(rt,bg="yellow")
c.bind("<B1-Motion>",painting)
c.bind("<Button-1>",start)
c.bind("<Button-3>",end)
c.pack()
rt.mainloop()
