import requests
from bs4 import BeautifulSoup

url1 = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%98%A4%EB%8A%98+%EC%9D%B8%EC%B2%9C+%EB%82%A0%EC%94%A8"
# url2 = "https://news.naver.com/"
# url3 = "https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=105&sid2=230"
# url4 - "https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english&keywd=haceng_submain_lnb_eng_I_others_english&logger_kw=haceng_submain_lnb_eng_I_others_english"

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
dusts = soap1.find("dd",attrs={"class":"lv2"})
dust = dusts.get_text()
very_dust = dusts.find_next_sibling("dd").get_text()


print("[오늘의 날씨]")
print(weather)
print("현재",temperature + "℃","  ","(최저",min_temperature,"/","최고",max_temperature+")")
print("오전 강수확률",am_rain,"%","/","오후 강수확률",pm_rain,"%")
print("")
print("미세먼지",dust)
print("초마세먼지",very_dust)
print("")


