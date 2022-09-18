import requests
from bs4 import BeautifulSoup

for i in range(1,6):
    url = 'https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=pnt&date=20220811&page='+str(i)
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser') # 구조화
    data = soup.select('div.tit5')
    scores = soup.select('td.point')
    for i,j in zip(data,scores): #zip 함수를 사용하여 짝을 지어준다.
        print(i.text.strip(), j.text.strip())

# 올해 마지막 날까지 남은 날 계산
import datetime
today = datetime.datetime.today()
lastday = datetime.datetime(2022, 12, 31)
print(lastday-today)

#100일 계산
dday = datetime.timedelta(dday=100)
print(today + dday)