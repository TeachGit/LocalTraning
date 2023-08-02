import random
from tkinter import *
import time

class Ball:
    def __init__(self, canvas, color, size):
        self.canvas = canvas
        self.id = self.canvas.create_oval(0, 0, size, size, fill=color)
        self.dx = random.randint(1, 10)
        self.dy = random.randint(1, 10)

    def move(self):
        self.canvas.move(self.id, self.dx, self.dy)
        x0, y0, x1, y1 = self.canvas.coords(self.id)

        if y1 > self.canvas.winfo_height() or y0 < 0:
            self.dy = -self.dy

        if x1 > self.canvas.winfo_width() or x0 < 0:
            self.dx = -self.dx


window = Tk()
canvas = Canvas(window, width=400, height=400)
canvas.pack()

ball1 = Ball(canvas, "blue", 60)
ball2 = Ball(canvas, "green", 100)
ball3 = Ball(canvas, "orange", 80)
ball4 = Ball(canvas, "red", 40)

while True:
    ball1.move()
    ball2.move()
    ball3.move()
    ball4.move()
    window.update()
    time.sleep(0.01)

window.mainloop()
