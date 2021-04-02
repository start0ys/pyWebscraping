import tkinter.ttk as ttk
from tkinter import *
root = Tk()            # tkinter를 이용하기위해서 해야하는 필수조건
root.title("시작")     #  실행이름
root.resizable(False,False)  #창크기(가로,세로) 값 변경불가

#메뉴 만들기 
menu=Menu(root)
#메모장 만들기 
def make():
    #버튼만들기(버튼)
    frame1=Frame(root)
    frame1.pack(fill="x")
    Button(frame1,text="오늘의 날씨",width=15,height=3).pack(side="left",padx=10)
    Button(frame1,text="실시간 검색어",width=15,height=3).pack(side="left",padx=95)
    Button(frame1,text="오늘의 웹툰",width=15,height=3).pack(side="left",padx=10)

    #문구 만들기
    frame1=Frame(root)
    frame1.pack(fill="x")
    Label(root,text="안녕하세요 자비스입니다.",font=15).pack(pady=10)
    #정보가져오기
    frame3=LabelFrame(root,text="정보")
    txt=Text(frame3) #frame안에 텍스트만들기
    txt.pack(side="left",expand="True",fill="both") #txt를 화면에 꽉차게 하기
    frame3.pack(fill="x")
    #종료 버튼
    frame4=Frame(root)
    Button(frame4,text="종료",padx=15,pady=10,command=root.quit).pack(side="right")
    frame4.pack(fill="x",pady=10)

#자비스 메뉴 만들기
menu_text=Menu(menu, tearoff=0)
menu_text.add_command(label="자비스 실행",command=make)
menu.add_cascade(label="자비스",menu=menu_text)
#게임 메뉴 만들기
menu_game=Menu(menu, tearoff=0)
menu_game.add_command(labe="게임 실행")
menu_game.add_separator()
menu_game.add_command(labe="게임 종료")
menu.add_cascade(label="게임",menu=menu_game)
#끝내기 메뉴 만들기
menu.add_cascade(label="끝내기",command=root.quit)

root.config(menu=menu) #메뉴 활성화
root.mainloop()        # tkinter를 이용하기위해서 해야하는 필수조건