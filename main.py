from tkinter import *
from PIL import Image, ImageTk

"""
대강 구성
frame별로 페이지 구성이 되어있다.
frame 안에 label 들어가고, label 안에 버튼과 구성요소들이 들어가있다.
frame 전환 함수들을 저렇게 무식하게 때려넣은 이유는... 내가 설계를 안하고 무식하게 하나하나 하다보니깐 저래 되었다.
"""
def openFrame(frame):
    frame.tkraise()

def specialmenu_open():
    openFrame(specialmenu_frame)
    
def premiummenu_open():
   openFrame(premiummenu_frame)

def newmenu_open():
   openFrame(newmenu_frame)
   
def whopermenu_open():
   openFrame(whopermenu_frame)
   
def chickenmenu_open():
   openFrame(chickenmenu_frame)
   
def alldaykingmenu_open():
   openFrame(alldaykingmenu_frame)
   
def sidemenu_open():
   openFrame(sidemenu_frame)
   
def drinkmenu_open():
   openFrame(drinkmenu_frame)   

#기본 Tk 구성요소
window = Tk()
window.title("main.py")
window.geometry("500x1200+100+100")

#여러가지 frame들 선언장소
home_frame = Frame(window)
specialmenu_frame = Frame(window)
premiummenu_frame = Frame(window)
newmenu_frame = Frame(window)
whopermenu_frame = Frame(window)
chickenmenu_frame = Frame(window)
alldaykingmenu_frame = Frame(window)
sidemenu_frame = Frame(window)
drinkmenu_frame = Frame(window)

#frame 기본 그리드설정
home_frame.grid(row=0, column=0, sticky="nsew")
specialmenu_frame.grid(row=0, column=0, sticky="nsew")
premiummenu_frame.grid(row=0, column=0, sticky="nsew")
newmenu_frame.grid(row=0, column=0, sticky="nsew")
whopermenu_frame.grid(row=0, column=0, sticky="nsew")
chickenmenu_frame.grid(row=0, column=0, sticky="nsew")
alldaykingmenu_frame.grid(row=0, column=0, sticky="nsew")
sidemenu_frame.grid(row=0, column=0, sticky="nsew")
drinkmenu_frame.grid(row=0, column=0, sticky="nsew")

#메인화면 구성요소 선언 장소 / 메인화면이 그냥 홈 화면이다. 이미지 따오고, 버튼 추가하고 버튼 frame에 넣어놨는데 라벨로 묶어버릴지 아니면 이미지 통합할지 고민중이다
#추후에 심영준이 수정 예정
mp_1_img = ImageTk.PhotoImage(Image.open("./img/mainpage/mainpage_1.png"))
mp_2_img = ImageTk.PhotoImage(Image.open("./img/mainpage/mainpage_2.png"))
mp_3_img = ImageTk.PhotoImage(Image.open("./img/mainpage/mainpage_3.png"))
mp_4_img = ImageTk.PhotoImage(Image.open("./img/mainpage/mainpage_4.png"))
mp_5_img = ImageTk.PhotoImage(Image.open("./img/mainpage/mainpage_5.png"))
mainpage_btn1 = Button(home_frame, image=mp_1_img, width=480, height=160, command=specialmenu_open)
mainpage_btn2 = Button(home_frame, image=mp_2_img, width=480, height=160, command=specialmenu_open)
mainpage_btn3 = Button(home_frame, image=mp_3_img, width=480, height=160, command=specialmenu_open)
mainpage_btn4 = Button(home_frame, image=mp_4_img, width=480, height=160, command=specialmenu_open)
mainpage_btn5 = Button(home_frame, image=mp_5_img, width=480, height=160, command=specialmenu_open)
mainpage_btn1.pack()
mainpage_btn2.pack()
mainpage_btn3.pack()
mainpage_btn4.pack()
mainpage_btn5.pack()

#헤더 관련 어쩌구... 일단 frame을 다 따로 나눈 이상 메뉴에서의 frame별 이동은 버튼클릭액션이 필수적이다. 바보같이 하나하나 노가다하는중
header_special_select_img = ImageTk.PhotoImage(Image.open("./img/menu_header/special_menu_select.png"))
header_special_non_img = ImageTk.PhotoImage(Image.open("./img/menu_header/special_menu_non.png"))
header_new_select_img = ImageTk.PhotoImage(Image.open("./img/menu_header/new_menu_select.png"))
header_new_non_img = ImageTk.PhotoImage(Image.open("./img/menu_header/new_menu_non.png"))
header_premium_select_img = ImageTk.PhotoImage(Image.open("./img/menu_header/premium_menu_select.png"))
header_premium_non_img = ImageTk.PhotoImage(Image.open("./img/menu_header/premium_menu_non.png"))
header_whoper_select_img = ImageTk.PhotoImage(Image.open("./img/menu_header/whoper_menu_select.png"))
header_whoper_non_img = ImageTk.PhotoImage(Image.open("./img/menu_header/whoper_menu_non.png"))
header_chicken_select_img = ImageTk.PhotoImage(Image.open("./img/menu_header/chicken_menu_select.png"))
header_chicken_non_img = ImageTk.PhotoImage(Image.open("./img/menu_header/chicken_menu_non.png"))
header_alldayking_select_img = ImageTk.PhotoImage(Image.open("./img/menu_header/alldayking_menu_select.png"))
header_alldayking_non_img = ImageTk.PhotoImage(Image.open("./img/menu_header/alldayking_menu_non.png"))
header_side_select_img = ImageTk.PhotoImage(Image.open("./img/menu_header/side_menu_select.png"))
header_side_non_img = ImageTk.PhotoImage(Image.open("./img/menu_header/side_menu_non.png"))
header_drink_select_img = ImageTk.PhotoImage(Image.open("./img/menu_header/drink_menu_select.png"))
header_drink_non_img = ImageTk.PhotoImage(Image.open("./img/menu_header/drink_menu_non.png"))

menu_header_special_label = Label(specialmenu_frame, width=500, height=150, bg="white")
menu_header_new_label = Label(newmenu_frame, width=500, height=150, bg="white")
menu_header_premium_label = Label(premiummenu_frame, width=500, height=150, bg="white")
menu_header_whoper_label = Label(whopermenu_frame, width=500, height=150, bg="white")
menu_header_chicken_label = Label(chickenmenu_frame, width=500, height=150, bg="white")
menu_header_alldayking_label = Label(alldaykingmenu_frame, width=500, height=150, bg="white")
menu_header_side_label = Label(sidemenu_frame, width=500, height=150, bg="white")
menu_header_drink_label = Label(drinkmenu_frame, width=500, height=150, bg="white")

#여긴 아직 헤더 미완성임 / 사이즈 조절중이니깐 천천히 바꾸겠음
header_special_select_btn = Button(menuheader_special_label, image=header_special_select_img, width=52, height=20, bg="white")
header_special_select_btn.pack(side="top")
menu_header_special_label.pack()

#스페셜 메뉴 화면 구성요소들 / 나중에 장바구니 담는 액션이 필요하다. 
menu_special_1_img = ImageTk.PhotoImage(Image.open("./img/menu/special_1.png"))
menu_special_2_img = ImageTk.PhotoImage(Image.open("./img/menu/special_2.png"))
menu_special_3_img = ImageTk.PhotoImage(Image.open("./img/menu/special_3.png"))
menu_special_4_img = ImageTk.PhotoImage(Image.open("./img/menu/special_4.png"))
specialmenu_1_label = Label(specialmenu_frame, width=500, height=150, bg="white")
specialmenu_2_label = Label(specialmenu_frame, width=500, height=150, bg="white")
specialmenu_1_btn = Button(specialmenu_1_label, image=menu_special_1_img, width=140, height=140, bg="white")
specialmenu_2_btn = Button(specialmenu_1_label, image=menu_special_2_img, width=140, height=140, bg="white")
specialmenu_3_btn = Button(specialmenu_1_label, image=menu_special_3_img, width=140, height=140, bg="white")
specialmenu_4_btn = Button(specialmenu_2_label, image=menu_special_4_img, width=140, height=140, bg="white")
specialmenu_1_btn.pack(side="left")
specialmenu_2_btn.pack(side="right")
specialmenu_3_btn.pack(side="right")
specialmenu_4_btn.pack(side="left")
specialmenu_1_label.pack()
specialmenu_2_label.pack()


#기본 실행
openFrame(home_frame)
window.mainloop()