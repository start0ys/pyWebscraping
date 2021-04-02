import requests
url = "http://naver.com"
header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"}
res = requests.get(url, headers=header)
res.raise_for_status() # 문제가 있다면 오류를 내준다 requsets를 해줄때는 보통 같이 써준다.
