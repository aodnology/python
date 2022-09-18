import requests
from bs4 import BeautifulSoup
import datetime
today = datetime.datetime.today()

for i in range(1,11):
    a = today - datetime.timedelta(days=i)
    b = a.strftime('%Y%m%d')
    url = 'https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=pnt&date='+b
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser') # 구조화
    data = soup.select('div.tit5')
    scores = soup.select('td.point')
    for i,j in zip(data,scores): #zip 함수를 사용하여 짝을 지어준다.
        print(i.text.strip(), j.text.strip())