import requests
import re
from bs4 import BeautifulSoup

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"}
for i in range(1,28): # 1페이지부터 27페이지까지
   
    url = "https://www.coupang.com/np/search?q=%EC%8A%A4%EB%A7%88%ED%8A%B8%EC%9B%8C%EC%B9%98&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=&backgroundColor=".format(i)
    res = requests.get(url, headers=headers)
    res.raise_for_status()

    soup = BeautifulSoup(res.text,"lxml") # 가져온 문서를 lxml을 통해 BeautifulSoup 객체로 만들기

    items = soup.find_all("li", attrs={"class":re.compile("^search-product")}) # 제품가져오기

    for item in items :
        link = "https://www.coupang.com" + item.a["href"] #링크 추가
        ad = item.find_all("span",attrs={"class":"ad-badge-text"}) #광고 제품가져오기
        if ad:
            continue  #만약 광고제품이면 다음거로 넘어가기
        name = item.find("div",attrs={"class":"name"}).get_text()  # 제품명 가져오기
        price = item.find("strong", attrs={"class":"price-value"}).get_text()  # 가격가져오기
        price = price.replace(",","") # 문자열 변경
        rate = item.find("em", attrs={"class":"rating"})  #평점 가져오기
        if rate:
            rate=rate.get_text()
        else:
            continue # 평점이 없으면 다음거로 넘어가기
        
        rate_num = item.find("span", attrs={"class":"rating-total-count"}) #평점수 가져오기
        if rate_num:     #(평점수)
            rate_num = rate_num.get_text()
            rate_num = rate_num[1:-1] #(평점수)이기때문에 처음인덱스와 마지막 인덱스를 제외해서 ()벗겨주기
        else:
            continue #평점수가 없으면 다음거로 넘어가기

        # 리뷰 500이상,평점 4.5이상만
        if float(rate) >= 4.5 and int(rate_num) >= 500 and int(price) < 300000:
            print ("제품명 :",name ,"",'\033[91m'+"가격 :",price,"원" +'\033[0m')
            print ('\033[91m'+"평점 :",rate ,"","평점수 :",rate_num +'\033[0m')
            print('\033[91m'+"링크 :"+'\033[0m',link)
            print("") 

    

    









