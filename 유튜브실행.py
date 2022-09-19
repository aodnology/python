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
driver = webdriver.Chrome(service=service, options=chrome_options) # 크롬 브라우저를 실행하는 것과 같은 코드
driver.get('https://www.youtube.com/')
driver.implicitly_wait(5) # 위 페이지가 로딩될때까지 기다리게 함
searchbox = driver.find_element(By.CSS_SELECTOR, 'input#search') # elements 는 여러개를 찾음 #CSS_SELECTOR로 찾음
searchbox.click()
searchbox.send_keys('힙합') # search 칸에 '' 안의 글자가 입력됨
searchbox.send_keys(Keys.ENTER) # 엔터키를 누른 것과 같은 코드
time.sleep(3) # 실행시 텀을 주는 것이 좋다 (시간 간격이 너무 짧거나 일정한 경우 로봇으로 인식함)
driver.find_element(By.CSS_SELECTOR, 'yt-formatted')
time.sleep(10)
driver.quit()

