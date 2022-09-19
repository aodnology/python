import requests
from bs4 import BeautifulSoup
url = 'https://www.melon.com/chart/index.htm'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')
data = soup.select('div.ellipsis.rank01') # 공백이 있는 경우 .으로 연결
print(data)