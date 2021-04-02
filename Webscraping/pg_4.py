import requests
import tkinter.ttk as ttk
from selenium import webdriver
from bs4 import BeautifulSoup
from tkinter import *

root = Tk()            # tkinter를 이용하기위해서 해야하는 필수조건
root.title("시작")     #  실행이름
root.resizable(False,False)  #창크기(가로,세로) 값 변경불가

url1 = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%98%A4%EB%8A%98+%EC%9D%B8%EC%B2%9C+%EB%82%A0%EC%94%A8"
url2 = "https://www.naver.com/"
url3 = "https://www.melon.com/chart/index.htm"

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"} 
###headless 크롬 설정 ###
options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36")

#오늘 날씨 가져오기
res1 = requests.get(url1)
res1.raise_for_status()

soap1 = BeautifulSoup(res1.text, "lxml")

weather = soap1.find("p",attrs={"class":"cast_txt"}).get_text()
temperature = soap1.find("span",attrs={"class":"todaytemp"}).get_text()
min_temperature = soap1.find("span",attrs={"class":"min"}).get_text()
max_temperature = soap1.find("span",attrs={"class":"max"}).get_text()
am_rain = soap1.find("span",attrs={"class":"point_time morning"}).find("span",attrs={"class":"num"}).get_text()
pm_rain = soap1.find("span",attrs={"class":"point_time afternoon"}).find("span",attrs={"class":"num"}).get_text()
dusts = soap1.find("dl",attrs={"class":"indicator"}).find_all("dd")
dust = dusts[0].get_text()
very_dust = dusts[1].get_text()

# 날씨 함수
def weathers():
     label1.config(text="오늘의 날씨",font=15) #라벨 변경
     txt.delete("1.0",END) #불러오기전에 txt내용들 다 지우기
    
     #불러온 내용을 txt에 삽입하기
     txt.insert(END, "[오늘의 날씨] \n") 
     txt.insert(END,"{}\n".format(weather))   
     txt.insert(END,"현재 {}℃    (최저 {} / 최고 {})\n".format(temperature,min_temperature,max_temperature)) 
     txt.insert(END,"오전 강수확률 {}% / 오후 강수확률 {}%\n".format(am_rain,pm_rain))
     txt.insert(END,"\n미세먼지 {}\n".format(dust)) 
     txt.insert(END,"초미세먼지 {}".format(very_dust)) 
     txt.insert(END,"\n\n\n\n\n\n\n") 
     #강수확률에 따라 멘트 추가
     if int(am_rain) == 0 and int(pm_rain) ==0:
        txt.insert(END,"오늘 날씨가 맑습니다.") 
     elif int(am_rain) == 0 and int(pm_rain) ==30:
        txt.insert(END,"오전에는 맑았다가 오후에 흐려집니다.") 
     elif int(am_rain) == 0 and int(pm_rain) > 30:
        txt.insert(END,"오전에는 맑았다가 오후에 비가옵니다.") 
        txt.insert(END,"\n오후 외출 시 우산을 챙겨주세요") 
     elif int(am_rain) == 30 and int(pm_rain) ==0:
        txt.insert(END,"오전에 흐렸다가 오후에 맑아집니다.") 
     elif int(am_rain) == 30 and int(pm_rain) ==30:
        txt.insert(END,"오늘 하루종일 흐립니다.") 
     elif int(am_rain) == 30 and int(pm_rain) >30:
        txt.insert(END,"오전에 흐렸다가 오후에 비가옵니다.")
        txt.insert(END,"\n오후 외출 시 우산을 챙겨주세요")  
     elif int(am_rain) > 30 and int(pm_rain) ==0:
        txt.insert(END,"오전에는 비가 오고 오후에 맑아집니다..") 
        txt.insert(END,"\n오전 외출 시 우산을 챙겨주세요") 
     elif int(am_rain) > 30 and int(pm_rain) ==30:
        txt.insert(END,"오전에는 비가 오고 오후내내 흐립니다.") 
        txt.insert(END,"\n오전 외출 시 우산을 챙겨주세요") 
     else:
        txt.insert(END,"오늘 하루종일 비가옵니다.") 
        txt.insert(END,"\n외출 시 우산을 챙겨주세요") 



#실시간 검색어 가져오기

def search():
   label1.config(text="실시간 검색어",font=15) #라벨 변경
   
   txt.delete("1.0",END) #불러오기전에 txt내용들 다 지우기  
   
   browser = webdriver.Chrome(options=options) #크롬 웹 드라이버 객체생성
   browser.get(url2) # 브라우저에서 네이버로 이동
   # 셀레니움으로 실시간검색어 들어가기
   browser.find_element_by_class_name("group_keyword").click()

   browser.find_element_by_xpath("//*[@id='NM_RTK_VIEW_filter_wrap']/li[1]/div/a[1]").click() #이슈 묶어보기 클릭
   browser.find_element_by_xpath("//*[@id='NM_RTK_VIEW_filter_wrap']/li[2]/div/a[1]").click() #이벤트.할인 클릭
   browser.find_element_by_xpath("//*[@id='NM_RTK_VIEW_filter_wrap']/li[3]/div/a[1]").click() #시사 클릭
   browser.find_element_by_xpath("//*[@id='NM_RTK_VIEW_filter_wrap']/li[4]/div/a[1]").click() #엔터 클릭
   browser.find_element_by_xpath("//*[@id='NM_RTK_VIEW_filter_wrap']/li[5]/div/a[1]").click() #스포츠 클릭

   browser.find_element_by_xpath("//*[@id='NM_RKT_VIEW_filter_age_wrap']/li[2]/a").click() 
   browser.find_element_by_xpath("//*[@id='NM_RTK_VIEW_set_btn']").click() 

   # 실시간검색어 정보가져오기

   soup2 = BeautifulSoup(browser.page_source,"lxml")

   rank_1_20 = soup2.find("div", attrs={"class":"realtime_box"}) #1위부터 10위 검색어 전체
   ranks_1_10 = rank_1_20.find_all("li")  #1위부터 10위검색어 전체에서 링크정보와 검색어 정보 있는곳
   ranks_11_20 = rank_1_20.find_next_sibling("div").find_all("li") #1위부터 10위 검색어 전체에서 11위부터 20위 검색에 전체로오고 링크정보와 검색어 정보가 있는곳으로 오기
   
   txt.insert(END,"[실시간 검색어]\n") 

   #1위부터 10위 가져오기
   for rank_1_10 , a in zip(ranks_1_10 , range(1,11)):
      search_1_10 = rank_1_10.find("span",attrs={"class":"keyword"}).get_text()
      link_1_10 = rank_1_10.a["href"]
      txt.insert(END,"{}위 :{}".format(a,search_1_10)) 
      txt.insert(END,"\n")
  
      # 관심있는 기사는 터미널에서 링크로 들어갈수있다
      print("{}위 :{}".format(a,search_1_10))
      print("링크 :{}".format(link_1_10))
      print("-"*50)
   #11위부터 20위가져오기
   for rank_11_20 , b in zip (ranks_11_20 , range(11,21)):
      search_11_20 = rank_11_20.find("span",attrs={"class":"keyword"}).get_text()
      link_11_20 = rank_11_20.a["href"]
      txt.insert(END,"{}위 :{}".format(b,search_11_20)) 
      txt.insert(END,"\n")
   
      # 관심있는 기사는 터미널에서 링크로 들어갈수있다  
      print("{}위 :{}".format(b,search_11_20))
      print("링크 :{}".format(link_11_20))
      print("-"*50)
  
   txt.insert(END,"\n\n----------------------[관심있는 기사는 터미널에서 링크확인]----------------------") 
   browser.quit() # 웹스크래핑이 끝나면 브라우저 닫기

#멜론 차트가져오기
def music():
    label1.config(text="멜론 차트",font=15) #라벨 변경
   
    txt.delete("1.0",END) #불러오기전에 txt내용들 다 지우기  
    res3 = requests.get(url3,headers=headers)
    res3.raise_for_status()

    soap3 = BeautifulSoup(res3.text, "lxml")


    all_songs = soap3.find("tr",attrs={"data-song-no":"33077590"})
    for num in range(1,11):
        
        song = all_songs.find("div",attrs={"class":"ellipsis rank01"}).get_text().strip()
        singer = all_songs.find("span",attrs={"class":"checkEllipsis"}).get_text().strip()
        txt.insert(END,"{}위 :{} \n아티스트 :{}\n".format(num,song,singer))


        all_songs = all_songs.find_next_sibling("tr")






#메뉴 만들기 
menu=Menu(root)
#메모장 만들기 
def make():
    #버튼만들기(버튼)
    frame1=Frame(root)
    frame1.pack(fill="x")
    Button(frame1,text="오늘의 날씨",width=15,height=3,command=weathers).pack(side="left",padx=10)
    Button(frame1,text="실시간 검색어",width=15,height=3,command=search).pack(side="left",padx=95)
    Button(frame1,text="멜론 차트",width=15,height=3,command=music).pack(side="left",padx=10)

    #문구 만들기
    frame1=Frame(root)
    frame1.pack(fill="x")
    global label1
    label1=Label(root,text="안녕하세요 자비스입니다.",font=15)
    label1.pack(pady=10)
    #정보가져오기
    frame3=LabelFrame(root,text="정보")
    global txt
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