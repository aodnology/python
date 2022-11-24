import requests
from bs4 import BeautifulSoup
import time
import random

# 검색 정보 입력
query = input('뉴스 검색어를 입력하세요 : ')
startdate = input('시작 날짜 (yyyy.mm.dd) : ')
lastdate = input('종료 날짜 (yyyy.mm.dd) : ')

# 십의 자리와 일의 자리 더하기 (page 번호 처리)


def solution(n):
    answer = 0
    n = list(map(int, str(n)))

    for i in range(len(n)):
        answer += n[i]
    return answer


# 크롤링
for num in range(1, 151, 10):
    url = 'https://search.naver.com/search.naver?where=news&query='+query+'&sort=0&photo=0&field=0&pd=3&ds='+startdate+'&de='+lastdate+'&cluster_rank=82&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:from'+startdate+'to'+lastdate+',a:all&start='+str(num)
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    data = soup.select('a.news_tit')
    num = solution(num)
    time.sleep(random.uniform(3,7)) #3~7초 사이 랜덤한 시간으로 크롤링 대기

# 크롤링 데이터 출력
    print(num, 'page')
    for i in data:
        print(startdate, i['href'], i['title'])
        