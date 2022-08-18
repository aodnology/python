import requests
from bs4 import BeautifulSoup
url = 'https://www.melon.com/chart/index.htm'

# 406error가 나는 경우 사용 (크롬에서 what is my user agent 검색) 
h = {'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}
res = requests.get(url, headers=h)
# headers를 사용하여 로봇이 아니라 브라우저라고 알려줌 이것도 안되는 경우에 selenum을 사용함
soup = BeautifulSoup(res.text, 'html.parser')
data = soup.select('div.ellipsis.rank01') # 공백은 .으로 연결 (원래 태그 == ellipsis rank01)
for i in data:
    print(i.text.strip()) #strip() == 공백 제거