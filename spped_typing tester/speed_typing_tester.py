import os
os.system=("cls")
from tkinter import *
root=Tk()
root.geometry("900x455")
root.configure(bg="grey")
root.title("#*Typing_Tester*#")
photo=PhotoImage(file="speed_typing_tester.png")
image_label=Label(image=photo)
image_label.pack()
text_label=Label(text="`START TYPING HERE`",fg="white",bg="black",font=("Helvetica",19),bd=1,relief="sunken")
text_label.pack()
root.mainloop()