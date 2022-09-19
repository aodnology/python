import requests
from bs4 import BeautifulSoup
url = 'http://movie.naver.com/movie/running/'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')
data = soup.select('dt.tit > a')
print(data)

for i in data:
    # print(i.text) #영화 이름만 원할때
    print('http://movie.naver.com/'+ i['href'])