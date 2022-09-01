import requests
# import bs4
from bs4 import BeautifulSoup # 웹에서 소스를 긁어올때 사용

#페이지의 모든 소스를 가져옮
url = 'https://weather.naver.com/'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')

#페이지의 원하는 소스의 정보를 가져옴
data = soup.select_one('strong.current')
print(data.text)