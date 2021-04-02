from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#headlesss크롬
options = webdriver.ChromeOptions()
options.headless = True

#셀레니움으로 다음 들어가기
browser = webdriver.Chrome(options = options)
url = "https://www.daum.net/"
browser.get(url)

#검색정보가져와서 '송파 헬리오시티'검색하기
search = browser.find_element_by_id("q")
search.send_keys("송파 헬리오시티") 
search.send_keys(Keys.ENTER)
# 웹 스크래핑
soap = BeautifulSoup(browser.page_source, "lxml")

deals = soap.find_all("td", attrs={"class":"col1"})
areas = soap.find_all("td", attrs={"class":"col2"})
prices = soap.find_all("td", attrs={"class":"col3"})
nums = soap.find_all("td", attrs={"class":"col4"})
floors = soap.find_all("td", attrs={"class":"col5"})

for deal,area,price,num,floor,a in zip (deals,areas,prices,nums,floors,range(1,6)) :
    print("=========매물 {}=========".format(a))
    print("거래 :",deal.get_text())
    print("면적 :",area.get_text(),"(공급/전용)")
    print("가격 :",price.get_text(),"(만원)")
    print("동 :",num.get_text())
    print("층 ",floor.get_text())


browser.quit()


