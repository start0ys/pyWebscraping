import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
###headless 크롬 설정 ###
options = webdriver.ChromeOptions()
options.headless = True
#####user agent 값이 바뀌는 경우도 있어서 user agent를 지정해주면 좋다
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36")

#####크롬을 띄우기전에#####
browser = webdriver.Chrome(options = options)  ###headless 크롬 적용
browser.maximize_window() # 창크기 전체로 키우기

url = "https://play.google.com/store/movies/top"
browser.get(url)

#스크롤 내리기
#셀레니움에서는 자바스크립트코드를 실행할수있다.
#browser.execute_script("window.scrollTo(0,1028)")   #(0,내리는위치) 이 코드는 처음높이부터 1028까지 스크롤을 내리라는것이다.
#browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")   #(0,내리는위치) 이 코드는 처음높이부터 마지막까지 스크롤을 내리라는것이다.

#위에서 내린 스크롤의 위치를 return해와서  그 위치 저장
pre_h = browser.execute_script("return document.body.scrollHeight")

while 1:   
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")   # 스크롤을 가장 아래로내림
    time.sleep(2) #영화가 업로드되는시간을 대기해줌
    cur_h = browser.execute_script("return document.body.scrollHeight")
    if cur_h == pre_h:
        break

    pre_h = cur_h


soup = BeautifulSoup(browser.page_source,"lxml")   #브라우저 페이지 정보를 가져와서 처리하기

movies =soup.find_all("div",attrs={"class":"Vpfmgd"})

for movie in movies:
    title = movie.find("div",attrs={"class":"WsMG1c nnK0zc"}).get_text()  #제목 가져오기
    action_mv = movie.find("div",attrs={"class":"KoLSrc"} ,text="액션/어드벤처") #장르가 액션/어드벤처인것 가져오기
    price = movie.find("div", attrs={"class":"zYPPle"}).get_text() #가격 가져오기
    link = "https://play.google.com"+ movie.a["href"] #링크가져오기
    if action_mv:  #만약 장르가 액션/어드벤처인게 있다면
        action_mv.get_text() #글자만 가져오기
    else: #장르가 액션/어드벤처가 아니라면
        continue #넘어가기
    print(title,"",'\033[91m'+"가격 :",price+'\033[0m')
    print('\033[91m'+"링크 : "+'\033[0m',link)
    print("-"*70)

browser.quit() # 웹스크래핑이 끝나면 브라우저 닫기
