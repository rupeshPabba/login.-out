import mysql.connector
import tkinter as tk
from datetime import datetime
from tkinter import messagebox


db=mysql.connector.connect(host="localhost",user="root",passwd="mysql123")
db1=mysql.connector.connect(host="localhost",user="root",passwd="mysql123")
mycursor=db.cursor()
mycursor1=db1.cursor()
mycursor.execute("use login_cred")
mycursor.execute("select name from credentials")
name_list=[]
for i in mycursor:
    name_list.append(i[0])
print(name_list)
mycursor1.execute("use login_cred")
mycursor1.execute("select id from credentials")
id_list=[]
for i in mycursor1:
    id_list.append(i[0])
# print(id_list)

root=tk.Tk()
root.title("login_info")
root.geometry("450x350")
img=tk.PhotoImage(file=r"C:\Users\Sampath\Pictures\Screenshots\multi (2).png")
label =tk.Label(root,image=img)
label.place(x=0,y=0)
def login():
    global name_info,id_info,d1,x
    name_info=E1.get()
    id_info=E2.get()
    d1=datetime.now()
    print("login is pressed")
    for i in id_list:
        if id_info==i:
            mycursor.execute("select name from credentials where id=?",(id_info))
            if name_info==mycursor:
                continue
        else:
            messagebox.showerror("showerror","look over your credentials....!!!!")
            root.destroy()
def logout():
    global f,d2
    d2=datetime.now()
    f=d2-d1
    f=f/3600
    root.destroy()

name_var=tk.StringVar()
pass_var=tk.StringVar()
l1=tk.Label(root,text="NAME",fg="black")
l1.grid(row=1,column=1)  
l2=tk.Label(root,text="ID",fg="black")
l2.grid(row=2,column=1)
E1=tk.Entry(root,textvariable=name_var)
E1.grid(row=1,column=2)
E2=tk.Entry(root,textvariable=pass_var)
E2.grid(row=2,column=2)
b1=tk.Button(root,text="LOGIN",fg="white",bg="blue",command=login)
b1.grid(row=4,column=1)
b2=tk.Button(root,text="LOGOUT",fg="white",bg="blue",command=logout)
b2.grid(row=4,column=2)
root.mainloop()