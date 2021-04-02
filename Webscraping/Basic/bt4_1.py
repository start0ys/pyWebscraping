import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list.nhn?titleId=731130&weekday=thu&page=1"
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text,"lxml") # 가져온 문서를 lxml을 통해 BeautifulSoup 객체로 만들기
toons = soup.find_all("td", attrs={"class":"title"}) #clss 속성이 title인 td엘리멘트 모두 가져오기 
rates1 = soup.find_all("div", attrs={"class":"rating_type"}) #clss 속성이 rating_type인 div엘리멘트 모두 가져오기 
total_rate1 = 0

url2= "https://comic.naver.com/webtoon/list.nhn?titleId=731130&weekday=thu&page=2"
res2 = requests.get(url2)
res2.raise_for_status()
soup2 = BeautifulSoup(res2.text,"lxml") # 가져온 문서를 lxml을 통해 BeautifulSoup 객체로 만들기
toons2 = soup2.find_all("td", attrs={"class":"title"}) #clss 속성이 title인 td엘리멘트 모두 가져오기 
rates2 = soup2.find_all("div", attrs={"class":"rating_type"}) #clss 속성이 rating_type인 div엘리멘트 모두 가져오기 
total_rate2 = 0

url3 = "https://comic.naver.com/webtoon/list.nhn?titleId=731130&weekday=thu&page=3"
res3 = requests.get(url3)
res3.raise_for_status()
soup3 = BeautifulSoup(res3.text,"lxml") # 가져온 문서를 lxml을 통해 BeautifulSoup 객체로 만들기
toons3 = soup3.find_all("td", attrs={"class":"title"}) #clss 속성이 title인 td엘리멘트 모두 가져오기 
rates3 = soup3.find_all("div", attrs={"class":"rating_type"}) #clss 속성이 rating_type인 div엘리멘트 모두 가져오기 
total_rate3 = 0

url4 = "https://comic.naver.com/webtoon/list.nhn?titleId=731130&weekday=thu&page=4"
res4 = requests.get(url4)
res4.raise_for_status()
soup4 = BeautifulSoup(res4.text,"lxml") # 가져온 문서를 lxml을 통해 BeautifulSoup 객체로 만들기
toons4 = soup4.find_all("td", attrs={"class":"title"}) #clss 속성이 title인 td엘리멘트 모두 가져오기 
rates4 = soup4.find_all("div", attrs={"class":"rating_type"}) #clss 속성이 rating_type인 div엘리멘트 모두 가져오기 
total_rate4 = 0

url5 = "https://comic.naver.com/webtoon/list.nhn?titleId=731130&weekday=thu&page=5"
res5 = requests.get(url5)
res5.raise_for_status()
soup5 = BeautifulSoup(res5.text,"lxml") # 가져온 문서를 lxml을 통해 BeautifulSoup 객체로 만들기
toons5 = soup5.find_all("td", attrs={"class":"title"}) #clss 속성이 title인 td엘리멘트 모두 가져오기 
rates5 = soup5.find_all("div", attrs={"class":"rating_type"}) #clss 속성이 rating_type인 div엘리멘트 모두 가져오기 
total_rate5 = 0

url6 = "https://comic.naver.com/webtoon/list.nhn?titleId=731130&weekday=thu&page=6"
res6 = requests.get(url6)
res6.raise_for_status()
soup6 = BeautifulSoup(res6.text,"lxml") # 가져온 문서를 lxml을 통해 BeautifulSoup 객체로 만들기
toons6 = soup6.find_all("td", attrs={"class":"title"}) #clss 속성이 title인 td엘리멘트 모두 가져오기 
rates6 = soup6.find_all("div", attrs={"class":"rating_type"}) #clss 속성이 rating_type인 div엘리멘트 모두 가져오기 
total_rate6 = 0

url7 = "https://comic.naver.com/webtoon/list.nhn?titleId=731130&weekday=thu&page=7"
res7 = requests.get(url7)
res7.raise_for_status()
soup7 = BeautifulSoup(res7.text,"lxml") # 가져온 문서를 lxml을 통해 BeautifulSoup 객체로 만들기
toons7 = soup7.find_all("td", attrs={"class":"title"}) #clss 속성이 title인 td엘리멘트 모두 가져오기 
rates7 = soup7.find_all("div", attrs={"class":"rating_type"}) #clss 속성이 rating_type인 div엘리멘트 모두 가져오기 
total_rate7 = 0

url8 = "https://comic.naver.com/webtoon/list.nhn?titleId=731130&weekday=thu&page=8"
res8 = requests.get(url8)
res8.raise_for_status()
soup8 = BeautifulSoup(res8.text,"lxml") # 가져온 문서를 lxml을 통해 BeautifulSoup 객체로 만들기
toons8 = soup8.find_all("td", attrs={"class":"title"}) #clss 속성이 title인 td엘리멘트 모두 가져오기 
rates8 = soup8.find_all("div", attrs={"class":"rating_type"}) #clss 속성이 rating_type인 div엘리멘트 모두 가져오기 
total_rate8 = 0


for toon,rate1 in zip(toons,rates1):
    title = toon.a.get_text()
    link = "https://comic.naver.com" + toon.a["href"] 
    rate=rate1.find("strong").get_text()
    print(title,'\033[91m'+"평점:",rate+'\033[0m')
    print(link)
    total_rate1+=float(rate)

for toon2,rate2 in zip(toons2,rates2):
    title2 = toon2.a.get_text()
    link2 = "https://comic.naver.com" + toon2.a["href"] 
    rate22=rate2.find("strong").get_text()
    print(title2,'\033[91m'+"평점:",rate22+'\033[0m')
    print(link2)
    total_rate2+=float(rate22)

for toon3,rate3 in zip(toons3,rates3):
    title3 = toon3.a.get_text()
    link3 = "https://comic.naver.com" + toon3.a["href"] 
    rate33=rate3.find("strong").get_text()
    print(title3,'\033[91m'+"평점:",rate33+'\033[0m')
    print(link3)
    total_rate3+=float(rate33)

for toon4,rate4 in zip(toons4,rates4):
    title4 = toon4.a.get_text()
    link4 = "https://comic.naver.com" + toon4.a["href"] 
    rate44=rate4.find("strong").get_text()
    print(title4,'\033[91m'+"평점:",rate44+'\033[0m')
    print(link4)
    total_rate4+=float(rate44)

for toon5,rate5 in zip(toons5,rates5):
    title5 = toon5.a.get_text()
    link5 = "https://comic.naver.com" + toon5.a["href"] 
    rate55=rate5.find("strong").get_text()
    print(title5,'\033[91m'+"평점:",rate55+'\033[0m')
    print(link5)
    total_rate5+=float(rate55)

for toon6,rate6 in zip(toons6,rates6):
    title6 = toon6.a.get_text()
    link6 = "https://comic.naver.com" + toon6.a["href"] 
    rate66=rate6.find("strong").get_text()
    print(title6,'\033[91m'+"평점:",rate66+'\033[0m')
    print(link6)
    total_rate6+=float(rate66)

for toon7,rate7 in zip(toons7,rates7):
    title7 = toon7.a.get_text()
    link7 = "https://comic.naver.com" + toon7.a["href"] 
    rate77=rate7.find("strong").get_text()
    print(title7,'\033[91m'+"평점:",rate77+'\033[0m')
    print(link7)
    total_rate7+=float(rate77)

for toon8,rate8 in zip(toons8,rates8):
    title8 = toon8.a.get_text()
    link8 = "https://comic.naver.com" + toon8.a["href"] 
    rate88=rate8.find("strong").get_text()
    print(title8,'\033[91m'+"평점:",rate88+'\033[0m')
    print(link8)
    total_rate8+=float(rate88)

total_rate = total_rate1 + total_rate2 + total_rate3 + total_rate4 + total_rate5 + total_rate6 + total_rate7 + total_rate8
total_len = len(toons) + len(toons2) + len(toons3) + len(toons4) + len(toons5) + len(toons6) + len(toons7) + len(toons8)
print("전체 평점 합 : ",total_rate)
print("전체 만화 수 : ",total_len)
print('\033[91m'+ "전체 평균 평점 : ",str(round(total_rate/total_len , 2)) +'\033[0m')