import os
os.system=("cls")
from tkinter import *
import random
from timeit import default_timer as timer 
from tkinter import messagebox
root=Tk()
root.geometry("500x500")
root.configure(bg="black")
root.title("#*Typing_Tester*#")

def check_result():
    answer=typing_entry.get("1.0","end-1c")
    end=timer()
    time_taken=end-start
    error=j=0
    wpm=len(answer)/5
    wpm=wpm-error
    wpm=int(wpm/(time_taken/60))
    result="AMAZING! YOU HAVE A SPEED OF "+str(wpm)+" WPM"
    
    if len(answer)==0:
        messagebox.showinfo("ERROR","enter the values")
    
    
    elif len(x[word])>=len(answer):
        error=len(x[word])-len(answer)
        for i in answer:
            if i==x[word][j]:
                pass
            else:
                error+=1
            j+=1
    elif len(answer)>=len(x[word]):
        error=len(answer)-len(x[word])
        for i in x[word]:
            if i==x[word][j]:
                pass
            else:
                error+=1
            j+=1
       
       
    messagebox.showinfo("SCORE!",result)
    print(time_taken)

def finish():
    root.destroy()    


 






f=open(r"C:\Users\RUPESH\Desktop\RUPESH PABBA\spped_test_words.txt")
words=f.readlines()
f.close()
wordey=str(words)
x=wordey.split(".")
#text_test=[words]
word=random.randint(0,10)





label2=Label(root,text=x[word],fg="white",bg="grey",wraplength=500,font=("comicsansms",12))
label2.grid(row=1,column=3)


typing_entry=Text(root,width=70,height=10,font=("comicsansms",12))
typing_entry.grid(row=2,column=3)

b1=Button(text="submit",fg="white",bg="grey",relief="sunken",command=check_result)
b1.grid(row=3,columnspan=4)
b2=Button(text="done!",fg="white",bg="grey",relief="sunken",command=finish)
b2.grid(row=3,columnspan=5)








start=timer()


root.mainloop()
