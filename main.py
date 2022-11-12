from tkinter import *
from PIL import Image, ImageTk

window = Tk()

window.title("main.py")
window.geometry("2000x1600+100+100")

mp_1_img = ImageTk.PhotoImage(Image.open("./img/mainpage_1.png"))
label = Label(window, image=mp_1_img, width=1500, height=500, fg="white")
label.pack()

window.mainloop()