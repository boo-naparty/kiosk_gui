from tkinter import *
from PIL import Image, ImageTk

def mainpg_to_menupg():
    print("page_change")
    
mainpg = Tk()

mainpg.title("main.py")
mainpg.geometry("500x1200+100+100")

mp_1_img = ImageTk.PhotoImage(Image.open("./img/mainpage/mainpage_1.png"))
mp_2_img = ImageTk.PhotoImage(Image.open("./img/mainpage/mainpage_2.png"))
mp_3_img = ImageTk.PhotoImage(Image.open("./img/mainpage/mainpage_3.png"))
mp_4_img = ImageTk.PhotoImage(Image.open("./img/mainpage/mainpage_4.png"))
mp_5_img = ImageTk.PhotoImage(Image.open("./img/mainpage/mainpage_5.png"))
mainpage_btn1 = Button(mainpg, image=mp_1_img, width=480, height=160, command=mainpg_to_menupg)
mainpage_btn2 = Button(mainpg, image=mp_2_img, width=480, height=160, command=mainpg_to_menupg)
mainpage_btn3 = Button(mainpg, image=mp_3_img, width=480, height=160, command=mainpg_to_menupg)
mainpage_btn4 = Button(mainpg, image=mp_4_img, width=480, height=160, command=mainpg_to_menupg)
mainpage_btn5 = Button(mainpg, image=mp_5_img, width=480, height=160, command=mainpg_to_menupg)
mainpage_btn1.pack()
mainpage_btn2.pack()
mainpage_btn3.pack()
mainpage_btn4.pack()
mainpage_btn5.pack()

mainpg.mainloop()