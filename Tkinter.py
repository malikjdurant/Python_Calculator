from tkinter import *

root = Tk()

def myClick():
    myLabel2 = Label(root, text="This was coded in Python")
    myLabel2.pack()

myLabel1 = Label(root, text="Calculator")
myLabel1.pack()

myButton = Button(root, text="Click", command=myClick)
myButton.pack()

root.mainloop()