# (Tkinter: linear search animation) Write a program that animates the linear
# search algorithm. Create a l that consists of 20 distinct numbers from 1 to
# 20 in a random order. The elements are displayed in a histogram, as shown in
# Figure 10.17. You need to enter a search key in the text field. Clicking the
# Step button causes the program to perform one comparison in the algorithm
# and repaints the histogram with a bar indicating the search position. When
# the algorithm is finished, display a dialog box to inform the user. Clicking the
# Reset button creates a new random l for a new start.
import random
from tkinter import * 
import tkinter.messagebox

class stpCtrl:
    def __init__(self):
        self.l = [x for x in range(1, 20)]
        self.reset()
        self.key = 0

    def reset(self):
        self.i = -1 
        self.done = False
        random.shuffle(self.l)
        self.drawAStep()

    def step(self):
        if self.done:
            tkinter.messagebox.showinfo("showinfo", "Key found")
            return

        if self.i == -1:
            self.i += 1
        self.drawAStep()

        if self.i >= 0 and self.l[self.i] == self.key:
            self.done = True
            tkinter.messagebox.showinfo("showinfo", "Key found")
        elif self.i >= len(self.l) - 1:
            tkinter.messagebox.showinfo("showinfo", "Key not found")
        else:
            self.i += 1  # Continue to the next

    def drawAStep(self):
        bg = 10
        canvas.delete("line")
        canvas.create_line(10, h - bg, w - 10, h - bg, tag="line")
        bw = (w - 20) / len(self.l)

        mcount = int(max(self.l))
        for i in range(len(self.l)):
            canvas.create_rectangle(i * bw + 10, (h - bg) * (1 - self.l[i] / (mcount + 4)),(i + 1) * bw + 10, h - bg, tag="line")
            canvas.create_text(i * bw + 10 + bw / 2,(h - bg) * (1 - self.l[i] / (mcount + 4)) - 8,text=str(self.l[i]), tag="line")

        if self.i >= 0:
            canvas.create_rectangle(self.i * bw + 10,(h - bg) * (1 - self.l[self.i] / (mcount + 4)),(self.i + 1) * bw + 10, h - bg, fill="red", tag="line")

def step():
    control.key = float(key.get())
    control.step()

def reset():
    control.reset()

window = Tk()
window.title("Linear Search Animation") 

w = 340
h = 150
radius = 2
canvas = Canvas(window, w=w, h=h)
canvas.pack()

frame = Frame(window)
frame.pack()

Label(frame, text="Enter key:").pack(side=LEFT)
key = StringVar()
Entry(frame, textvariable=key, justify=RIGHT, w=3).pack(side=LEFT)
Button(frame, text="Step", command=step).pack(side=LEFT)
Button(frame, text="Reset", command=reset).pack(side=LEFT)
control = stpCtrl()
control.drawAStep()
window.mainloop() 
