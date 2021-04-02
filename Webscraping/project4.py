import requests
from bs4 import BeautifulSoup

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"}

url1 = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%98%A4%EB%8A%98+%EC%9D%B8%EC%B2%9C+%EB%82%A0%EC%94%A8"
url2 = "https://news.naver.com/"
url3 = "https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=105&sid2=230"
url4 = "https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english&keywd=haceng_submain_lnb_eng_I_others_english&logger_kw=haceng_submain_lnb_eng_I_others_english"

# 오늘 날씨 가져오기
res1 = requests.get(url1,headers=headers)
res1.raise_for_status()

soap1 = BeautifulSoup(res1.text, "lxml")

weather = soap1.find("p",attrs={"class":"cast_txt"}).get_text()
temperature = soap1.find("span",attrs={"class":"todaytemp"}).get_text()
min_temperature = soap1.find("span",attrs={"class":"min"}).get_text()
max_temperature = soap1.find("span",attrs={"class":"max"}).get_text()
am_rain = soap1.find("span",attrs={"class":"point_time morning"}).find("span",attrs={"class":"num"}).get_text() #오전 강수량과 오후 강수량의 class속성이같아서
pm_rain = soap1.find("span",attrs={"class":"point_time afternoon"}).find("span",attrs={"class":"num"}).get_text()#부모가달라서 부모부터 찾고 class속성으로찾기
dusts = soap1.find("dd",attrs={"class":"lv2"})#미세먼지
dust = dusts.get_text() 
very_dust = dusts.find_next_sibling("dd").get_text()#초미세먼지는 미세먼지와 xpath가 동일한 형제여서 next_sibling으로 찾아줌


print("[오늘의 날씨]")
print(weather)
print("현재",temperature + "℃","  ","(최저",min_temperature,"/","최고",max_temperature+")")
print("오전 강수확률",am_rain,"%","/","오후 강수확률",pm_rain,"%")
print("")
print("미세먼지",dust)
print("초마세먼지",very_dust)
print("")

# 헤드라인 뉴스 3건 가져오기
res2 = requests.get(url2,headers=headers)
res2.raise_for_status()

soap2 = BeautifulSoup(res2.text, "lxml")

total = soap2.find("ul",attrs={"class":"hdline_article_list"}).find("li") #헤드라인 뉴스 전체 가져오기
#첫번째 뉴스
title1s = total.find("div",attrs={"class":"hdline_article_tit"})
title1 = title1s.get_text().strip()
link1 = "https://news.naver.com"+ title1s.a["href"]
#첫번째 뉴스에서 다음 뉴스로 넘어가기위한 과정
step = total.find_next_sibling("li")
#두번째 뉴스
title2s = step.find("div",attrs={"class":"hdline_article_tit"}) #넘어온곳에서 뉴스제목 찾아주기
title2 = title2s.get_text().strip()
link2 = "https://news.naver.com"+ title2s.a["href"]
#세번째 뉴스
title3s = step.find_next_sibling("li").find("div",attrs={"class":"hdline_article_tit"}) #넘어온과정에서 한번 더 넘어서 뉴스제목찾아주기
title3 = title3s.get_text().strip()
link3 = "https://news.naver.com"+ title3s.a["href"]

print("[헤드라인 뉴스]")
print("1.",title1)
print(" ","(링크 :",link1 +")")
print("2.",title2)
print(" ","(링크 :",link2 +")")
print("3.",title3)
print(" ","(링크 :",link3 +")")
print("")

# IT뉴스 3건 가져오기
res3 = requests.get(url3,headers=headers)
res3.raise_for_status()

soap3 = BeautifulSoup(res3.text, "lxml")

it_total = soap3.find("ul",attrs={"class":"type06_headline"}).find("li") 
#첫번째 뉴스
news_1 = it_total.find("dl") #사진 정보를 찾으려면("dl")에서 찾아야한다
it_title1s = news_1.find("dt") #링크정보와 기사제목 정보를 찾으려면 ("dt")에서 찾아줘야한다

no_photo1 = news_1.find("dt",attrs={"class":"photo"}) 
if no_photo1 :                                #("dl")에 만약 사진이있다면
    it_title1 = it_title1s.img["alt"]      # img["alt"] 형식으로 출력 
else:                                      #없다면
    it_title1 = it_title1s.get_text().strip()   #text형식으로 출력

it_link1 = it_title1s.a["href"]

#다음 뉴스로 가기위한 과정
it_step = it_total.find_next_sibling("li")     # li부분에서 넘어가야한다 그래서 total("li")

#두번째 뉴스
news_2 = it_step.find("dl")
it_title2s = news_2.find("dt")

no_photo2 = news_2.find("dt",attrs={"class":"photo"})
if no_photo2 :
    it_title2 = it_title2s.img["alt"]
else:
    it_title2 = it_title2s.get_text().strip()

it_link2 = it_title2s.a["href"]

#세번째 뉴스
news_3 = it_step.find_next_sibling("li").find("dl")  #과정에서 한던더 넘어가고 dl찾기
it_title3s = news_3.find("dt")

no_photo3 = news_3.find("dt",attrs={"class":"photo"})
if no_photo3 :
    it_title3 = it_title3s.img["alt"]
else:
    it_title3 = it_title3s.get_text().strip()

it_link3 = it_title3s.a["href"]


print("[IT 뉴스]")
print("1.",it_title1)
print(" ","(링크 :",it_link1 +")")
print("2.",it_title2)
print(" ","(링크 :",it_link2 +")")
print("3.",it_title3)
print(" ","(링크 :",it_link3 +")")
print("")

# 오늘의 영어 회화 가져오기
res4 = requests.get(url4,headers=headers)
res4.raise_for_status()

soap4 = BeautifulSoup(res4.text, "lxml")

kr_talk = soap4.find("div",attrs={"class":"conv_txtBox"}) # 한글지문 가져오기
eng_talk = kr_talk.find_next_sibling("div") #한글 지문에서 이동한 후 영어지문 가져오기

print("[오늘의 영어 회화]")
print("(영어 지문)")
for a in range(2,50): #지문이 몇개가있을지 모르기때문에 크게 잡아두었다.
    eng = eng_talk.find("div",attrs={"id":"conv_kor_t{}".format(a)}).get_text().strip() #현재 글
    print(eng) #현재 글 print
    eng = eng_talk.find("div",attrs={"id":"conv_kor_t{}".format(a+1)}) #다음 글
    if eng: #만약 다음 글이있다면 pass
        pass 
    else:   #없다면 break 탈출
        break    
print("")
print("(한글 지문)")
for b in range(2,50):
    krs = kr_talk.find("div",attrs={"id":"conv_kor_t{}".format(b)}).get_text().strip()
    print(krs)
    krs = kr_talk.find("div",attrs={"id":"conv_kor_t{}".format(b+1)})
    if krs:
        pass
    else:
        break












