from itertools import product
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager #크롬 드라이버 자동 업데이트
import time
import pyautogui
import pyperclip

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

driver.get('https://www.instagram.com/')
driver.implicitly_wait(5)
idbox = driver.find_element(By.CSS_SELECTOR, 'input._2hvTZ.pexuQ.zyHYP')
idbox.click()
pyperclip.copy('myiD') # 인스타 아이디 입력
pyautogui.hotkey('ctrl', 'v')
time.sleep(0.5)
pwbox = driver.find_element(By.NAME, 'password')
pwbox.click()
pyperclip.copy('1234') # 비밀번호 입력
pyautogui.hotkey('ctrl', 'v')
# pwbox.send_keys('01gmlwls')
time.sleep(5)
pwbox.send_keys(Keys.ENTER)
time.sleep(5)

driver.get('https://www.instagram.com/explore/tags/에이블톤')
driver.implicitly_wait(10)
# elems = driver.find_element(By.CSS_SELECTOR, 'a.oajrlxb2')
# elems.click()
# time.sleep(3)
# driver.find_element(By.CSS_SELECTOR, 'span._aamw > button').click()
# time.sleep(5)
# driver.find_element(By.CSS_SELECTOR, 'div._aaqg._aaqh > button').click()
# time.sleep(4)
driver.find_element(By.CSS_SELECTOR, 'a.oajrlxb2').click()
time.sleep(2)   
for i in range(10):
    driver.find_element(By.CSS_SELECTOR, 'span._aamw > button').click()
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, 'div._aaqg._aaqh > button').click()
    time.sleep(4)
    print('좋아요')

driver.quit()