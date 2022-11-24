from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager #크롬 드라이버 자동 업데이트
import time
# 브라우저 꺼짐 방지 옵션
chrome_options = Options()
chrome_options.add_experimental_option('detach', True)
# chrome_options.add_argument('headless')
#불필요한 에러 메세지 없애기
chrome_options.add_experimental_option('excludeSwitches',['enable-logging'])
# 셀레니움으로 웹브라우저를 자동으로 띄움.
# service 객체를 만들고, 최신버전의 웹드라이버를 가져온다.  
# 크롬드라이버 매니저를 통해서
service = Service(executable_path=ChromeDriverManager().install())
# 서비스로 셀레니움 웹드라이버를 만듭니다.
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get('https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=101#&date=%2000:00:00&page=1')
driver.implicitly_wait(5)
from bs4 import BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')
data = soup.select('div.cluster_text')
for i in data:
    title = i.select_one('a')
    # link = title['href']
    print(title.text)

# data2 = soup.select('ul.type06') 
# #print(len(data2))
# for i in data2:
#     temp = i.select('dt>a') 
#     for t in temp:
#         print(t.text)

time.sleep(1)
driver.quit()