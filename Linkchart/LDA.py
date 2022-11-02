import requests
from bs4 import BeautifulSoup

for page in range(1, 3):
    url = 'https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=101#&date=%2000:00:00&page='+str(page)
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    data = soup.select('div.selection_body > ul > li')
    for i in data:
        print(i)

