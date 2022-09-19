# 기사 여러 페이지 가져오기
import requests
from bs4 import BeautifulSoup

query = input('뉴스 검색 : ')
for num in range(1, 102, 10): 
    url = 'https://search.naver.com/search.naver?where=news&sm=tab_jum&query='+query+'&sort=0&photo=0&field=0&pd=0&ds=&de=&cluster_rank=126&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:all,a:all&start='+str(num)
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    data = soup.select('a.news_tit')
    for i in data:
        print(i['href'], i['title'])
        #print(i.text)