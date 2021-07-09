import tkinter as tk
from tkinter import  *
from tkinter.filedialog import askopenfile
from tkinter.filedialog import asksaveasfile
from time import sleep
import os



def save(f,text):
    try:
        datas=text.get("1.0","end")
        ext=[('Python','*.py'),('Text','*.txt'),('C++','*.cpp')]
        file=asksaveasfile(filetypes=ext,defaultextension=ext)
        file.write(datas)
        file.close()
    except:
        pass
    
def text1(data,f):
    mylabel=Label(root)
    mylabel.place(x=0,y=30)
    text=Text(mylabel,cursor="plus",width=165,height=50)
    text.grid(row=0,column=0)
    scrollbar=Scrollbar(mylabel,command=text.yview)
    text.config(yscrollcommand=scrollbar.set)
    scrollbar.grid(row=0,column=1,sticky=NSEW)
    text.insert(END,data)
    Button(f,text="Save",width=10,command=lambda :save(f,text)).place(x=164,y=0)

    

def newfile():
    text1("",f)
    return

def fileopen(f):
    try:
        for widget in root.winfo_children():
            widget.destroy()
        f=Frame(root,width=1350,height=25,bg="grey").place(x=0,y=0)
        Button(f,text="New file",width=10,command=newfile).place(x=0,y=0)
        Button(f,text="open",width=10,command=lambda:fileopen(f)).place(x=82,y=0)
        file = askopenfile()
        data=file.read()
        text1(data,f)
    except:
        pass
    

root=tk.Tk()
root.title("Text Editor")
root.geometry('1350x768')
f=Frame(root,width=1350,height=25,bg="grey").place(x=0,y=0)
Button(f,text="New file",width=10,command=newfile).place(x=0,y=0)
Button(f,text="open",width=10,command=lambda:fileopen(f)).place(x=82,y=0)

root.mainloop()