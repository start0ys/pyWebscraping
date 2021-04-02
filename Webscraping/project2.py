import requests
from bs4 import BeautifulSoup

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"}

url1 = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%98%A4%EB%8A%98+%EC%9D%B8%EC%B2%9C+%EB%82%A0%EC%94%A8"
url2 = "https://news.naver.com/"
# url3 = "https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=105&sid2=230"
# url4 - "https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english&keywd=haceng_submain_lnb_eng_I_others_english&logger_kw=haceng_submain_lnb_eng_I_others_english"

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

# 헤드라인 뉴수 3건 가져오기
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