import requests
from bs4 import BeautifulSoup

url = 'https://news.naver.com/?viewType=pc'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')
data = soup.select('a.cjs_news_a._cds_link._editn_link')
print(data[0])

for i in data:
    title = i.select_one('div.cjs_t')
    link = i['href'] # i 에 href의 내용을 담음
    print(title.text, link)