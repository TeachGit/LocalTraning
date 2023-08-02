from tkinter import *


def button1click():
    print("Button 1 is Click")


def button2click():
    print("Button 2 is Click")


def button3click():
    print("Button 3 is Click")


def button4click():
    print("Button 4 is Click")


window = Tk()
bt1 = Button(window, text="Button1", bg="red", fg="white", command=button1click)
bt2 = Button(window, text="Button2", bg="green", fg="white", command=button1click)
bt3 = Button(window, text="Button3", bg="orange", fg="white", command=button1click)
bt4 = Button(window, text="Button4", bg="pink", fg="white", command=button1click)
bt1.grid(row=0, column=0)
bt2.grid(row=0, column=1)
bt3.grid(row=1, column=0)
bt4.grid(row=1, column=1)
window.mainloop()
