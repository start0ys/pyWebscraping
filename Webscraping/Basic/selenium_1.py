
from selenium import webdriver
from selenium.webdriver.common.keys import Keys  #키보드 입력을 위한 모듈
browser = webdriver.Chrome() #크롬 웹 드라이버 객체생성
browser.get("http://naver.com") # 브라우저에서 네이버로 이동


elem = browser.find_element_by_name("query")
elem.send_keys("안녕하세요") #키보드로 작성
elem.send_keys(Keys.ENTER) #엔터
elem = browser.find_element_by_name("query").clear() #엘리멘트부분 초기화 , 여기서는 검색한 글자 초기화로 없애기
elem = browser.find_element_by_name("query")
elem.send_keys("시작입니다") #키보드로 작성
elem.send_keys(Keys.ENTER) #엔터

# elem = browser.find_element_by_class_name("link_login")






elem.click() # 엘리멘트부분을 클릭하기
browser.back() # 뒤로가기
browser.forward() # 다시 앞으로가기
browser.refresh() # 새로고침
browser.close() # 브라우저의 현재 탭만 끄기
browser.quit() # 브라우저 전체 끄기