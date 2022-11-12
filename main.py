from tkinter import *
from PIL import Image, ImageTk

def openFrame(frame):
    frame.tkraise()

def mainpg_to_menupg():
    openFrame(mainmenu_frame)
    
window = Tk()

window.title("main.py")
window.geometry("500x1200+100+100")

home_frame = Frame(window)
mainmenu_frame = Frame(window)

home_frame.grid(row=0, column=0, sticky="nsew")
mainmenu_frame.grid(row=0, column=0, sticky="nsew")

mp_1_img = ImageTk.PhotoImage(Image.open("./img/mainpage/mainpage_1.png"))
mp_2_img = ImageTk.PhotoImage(Image.open("./img/mainpage/mainpage_2.png"))
mp_3_img = ImageTk.PhotoImage(Image.open("./img/mainpage/mainpage_3.png"))
mp_4_img = ImageTk.PhotoImage(Image.open("./img/mainpage/mainpage_4.png"))
mp_5_img = ImageTk.PhotoImage(Image.open("./img/mainpage/mainpage_5.png"))
mainpage_btn1 = Button(home_frame, image=mp_1_img, width=480, height=160, command=mainpg_to_menupg)
mainpage_btn2 = Button(home_frame, image=mp_2_img, width=480, height=160, command=mainpg_to_menupg)
mainpage_btn3 = Button(home_frame, image=mp_3_img, width=480, height=160, command=mainpg_to_menupg)
mainpage_btn4 = Button(home_frame, image=mp_4_img, width=480, height=160, command=mainpg_to_menupg)
mainpage_btn5 = Button(home_frame, image=mp_5_img, width=480, height=160, command=mainpg_to_menupg)
mainpage_btn1.pack()
mainpage_btn2.pack()
mainpage_btn3.pack()
mainpage_btn4.pack()
mainpage_btn5.pack()

openFrame(home_frame)
window.mainloop()