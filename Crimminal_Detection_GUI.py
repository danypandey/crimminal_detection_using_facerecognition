from tkinter import *
import os
from datetime import datetime;

root=Tk()

root.configure(background="white")

#root.geometry("300x300")
    
def function1():
    
    os.system("py DataBase_Creation.py")

def function2():

    os.system("py Detect_Crimminal.py")

def function3():

    root.destroy()
    
#stting title for the window
root.title("CRIMMINAL DETECTION USING FACE RECOGNITION")

#creating a text label
Label(root, text="CRIMMINAL DETECTION USING FACE RECOGNITION",font=("times new roman",20),fg="black",bg="red",height=2).grid(row=0,rowspan=2,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating first button
Button(root,text="Create Dataset",font=("times new roman",20),bg="#0D47A1",fg='black',command=function1).grid(row=3,columnspan=2,sticky=W+E+N+S,padx=5,pady=5)

#creating second button
Button(root,text="Train and Detect",font=("times new roman",20),bg="#0D47A1",fg='black',command=function2).grid(row=4,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

Button(root,text="Exit",font=('times new roman',20),bg="green",fg="black",command=function3).grid(row=9,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)


root.mainloop()
