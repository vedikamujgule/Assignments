# 14.5 (Tkinter: Count the occurrences of each letter) Revise the preceding exercise to
# display a histogram for the result, as shown in Figure 14.4. You need to display a
# message in a message box if the file does not exist.
from tkinter import *
import tkinter.messagebox
from tkinter.filedialog import askopenfilename

width = 23
b = 350
def showResult():
    file = open(filename.get(), 'r')
    lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].lower()
    countArray = [0] * 26
    countNOLetters(lines, countArray)
    cnvs.delete("data")
    cnvs.create_line(10, b, 595, b, tag="data")
    x = 12
    for i in range(26):
        cnvs.create_text(x+2, b+8, text=chr(i + ord('a')),tag="data")
        cnvs.create_rectangle(x-9, b-countArray[i], x + width-9, b,tag="data")
        x += width

def countNOLetters(lines, countArray):
    for line in lines:
        for ch in line:
            if ch.isalpha():
                countArray[ord(ch) - ord('a')] += 1

def openFile():
    filenameforReading = askopenfilename()
    filename.set(filenameforReading)

window = Tk() 
window.title("Occurrence of Letters") 
frame1 = Frame(window) 
frame1.pack()
cnvs = Canvas(frame1, width=600,height=400)
cnvs.pack()
frameSecond = Frame(window) 
frameSecond.pack()
Label(frameSecond, text="Enter a filename: ").pack(side=LEFT)
filename = StringVar()
Entry(frameSecond, width=20, textvariable=filename).pack(side=LEFT)
Button(frameSecond, text="Browse", command=openFile).pack(side=LEFT)
Button(frameSecond, text="Show Result", command=showResult).pack(side=LEFT)
window.mainloop()  