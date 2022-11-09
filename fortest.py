from tkinter import *
from math import *

window = Tk()
window.title("for test.py")
window.geometry("640x480+100+100")
window.resizable(False, False)

def calc(event):
    label.config(text="결과="+str(eval(entry.get())))
    
entry = Entry(window)
entry.bind("<Return>", calc)
entry.pack()

label = Label(window)
label.pack()

window.mainloop()