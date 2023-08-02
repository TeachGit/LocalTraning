from tkinter import *

window = Tk()


class Counter:
    def __init__(self):
        self.count = 0

    def increase(self):
        self.count += 1

    def reset(self):
        self.count = 0

    def getCount(self):
        return self.count


count = Counter()


def btIncrease():
    count.increase()
    entryValue.delete(0, 'end')
    entryValue.insert(0, str(count.getCount()))


def btReset():
    count.reset()
    entryValue.delete(0, 'end')
    entryValue.insert(0, str(count.getCount()))


btIncre = Button(window, text="Increase", command=btIncrease)
btReset = Button(window, text="Reset", command=btReset)
lb = Label(window, text="Value")
entryValue = Entry(window)
btIncre.grid(row=0, column=0)
btReset.grid(row=0, column=1)
lb.grid(row=1, column=0)
entryValue.grid(row=1, column=1)
window.mainloop()
