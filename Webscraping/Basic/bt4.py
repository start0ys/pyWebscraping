import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml") # 가져온 문서를 lxml을 통해 BeautifulSoup 객체로 만들기
print(soup.title)     # soup안의 정보에서 title이있는 엘리멘트 가져오기
print(soup.title.get_text()) #가져온title 엘리멘트에서 글자만 보기
# print(soup.a) # 첫번째로 발견되는 a엘리멘트 가져오기
# print(soup.a.attrs) #a 엘리멘트를 속성별로 사전 형태로 가져오기
# print(soup.a["href"]) #a 엘리멘트의 href속성의 값을 가져온다.
# print(soup.find("a", attrs={"class":"Nbtn_upload"}))  #class = "Nbtn_upload" 중에서 첫번째로 발견 되는 a 엘리멘트 가져오기
# print(soup.find(attrs={"class":"Nbtn_upload"}))  #class = "Nbtn_upload" 인 어떤 엘리멘트 가져오기

rank1 = soup.find("li",attrs={"class":"rank01"})
rank2 = rank1.next_sibling.next_sibling # 두번한이유 태그사이에 개행정보(줄바꿈)가있기때문에 개행정보(줄바꿈)을 표시한다 그래서 두번해주면된다.
# n_rank2=rank1.find_next_sibling("li")
# p_rank1 = rank2.previous_sibling.previous_sibling
# pp_rank1=rank2.find_previous_sibling("li")
# print(rank1)
# print(rank1.a.get_text())
print(rank2.a.get_text())
# print(p_rank1.a.get_text())
# print(rank1.parent)
# print(n_rank2)
# print(rank2)
# print(pp_rank1)
# all_rank=rank1.find_next_siblings("li")
# print(all_rank)
# webtoon = soup.find("a", text="싸움독학-62화 : 실전의 무도")
# print(webtoon)


