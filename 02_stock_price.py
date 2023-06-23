import requests # 정보 달라고 웹에 요청
from bs4 import BeautifulSoup # 가져온 정보를 parsing 하기
# 주식 가격 가져오기
'''
038880, 005930, 086520
'''
finance_list = [('038880', '아이에이'), ('005930', "삼성전자"), ('086520', "에코프로")]
for i in finance_list :
    url = f"https://finance.naver.com/item/sise.naver?code={i[0]}"
    response = requests.get(url)
    html = response.text

    soup = BeautifulSoup(html, 'html.parser')

    price = soup.select_one("strong#_nowVal.tah.p11")
    print(i[1] + " 의 가격은 : ", end="$")
    print(price.text)