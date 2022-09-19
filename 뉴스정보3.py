import requests
from bs4 import BeautifulSoup
while True:
    query = input('뉴스 검색 : ')
    if query == 'end':
        break
    url = 'https://search.naver.com/search.naver?where=news&sm=tab_jum&query='+query
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    data = soup.select('a.news_tit')
    for i in data:
        print(i['href'], i['title'])
        #print(i.text)