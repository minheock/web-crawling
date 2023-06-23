import requests 
from bs4 import BeautifulSoup 


movieUrl = "https://entertain.naver.com/movie"

response = requests.get(movieUrl)
html = response.text

soup = BeautifulSoup(html, "html.parser")
articletitles = soup.select("a.tit")
keymovie = input("키워드를 입력하세요 : ")

for i in articletitles :
    saveTitle = i.text
    if saveTitle.count(keymovie) > 0 :
        print(saveTitle)