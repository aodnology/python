import requests
from bs4 import BeautifulSoup

url = 'https://search.naver.com/search.naver?where=news&sm=tab_jum&query=공모전'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')
data = soup.select('a.news_tit')
for i in data:
    print(i['href'], i['title'])
    #print(i.text)