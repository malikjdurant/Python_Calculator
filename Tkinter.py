from tkinter import *

root = Tk()

#def myClick():
    #myLabel2 = Label(root, text="This was coded in Python")
    #myLabel2.pack()

myLabel1 = Label(root, text="Calculator")
myLabel1.grid(row=0, column=1)

myButton1 = Button(root, text="1")
myButton2 = Button(root, text="2")
myButton3 = Button(root, text="3")
myButton4 = Button(root, text="4")
myButton5 = Button(root, text="5")
myButton6 = Button(root, text="6")
myButton7 = Button(root, text="7")
myButton8 = Button(root, text="8")
myButton9 = Button(root, text="9")
myButton0 = Button(root, text="0")

myButton1.grid(row=3, column=0)
myButton2.grid(row=3, column=1)
myButton3.grid(row=3, column=2)
myButton4.grid(row=2, column=0)
myButton5.grid(row=2, column=1)
myButton6.grid(row=2, column=2)
myButton7.grid(row=1, column=0)
myButton8.grid(row=1, column=1)
myButton9.grid(row=1, column=2)
myButton0.grid(row=4, column=1)

root.mainloop()