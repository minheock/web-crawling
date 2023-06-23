import requests # 정보 달라고 웹에 요청
from bs4 import BeautifulSoup # 가져온 정보를 parsing 하기
# 주식 가격 가져오기

url = "https://finance.naver.com/item/sise.naver?code=005930"
response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, 'html.parser')

price = soup.select_one("strong#_nowVal.tah.p11")
print(price.text)