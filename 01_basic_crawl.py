import requests # 정보 달라고 웹에 요청
from bs4 import BeautifulSoup # 가져온 정보를 parsing 하기

response = requests.get("https://finance.naver.com/")
html = response.text

soup = BeautifulSoup(html, 'html.parser')

result = soup.select_one(".h_market")
print(result.text)
