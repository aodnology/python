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
# headless 사용시 브라우저를 띄우지 않고 정보만 찾아옴
#불필요한 에러 메세지 없애기
chrome_options.add_experimental_option('excludeSwitches',['enable-logging'])
# 셀레니움으로 웹브라우저를 자동으로 띄움.
# service 객체를 만들고, 최신버전의 웹드라이버를 가져온다.  
# 크롬드라이버 매니저를 통해서
service = Service(executable_path=ChromeDriverManager().install())
# 서비스로 셀레니움 웹드라이버를 만듭니다.
driver = webdriver.Chrome(service=service, options=chrome_options) # 크롬 브라우저를 실행하는 것과 같은 코드
driver.get('https://shopping.naver.com/home/p/index.naver')
driver.implicitly_wait(7)
searchbox = driver.find_element(By.CSS_SELECTOR, 'input._searchInput_search_input_QXUFf')
searchbox.click()
searchbox.send_keys('아이폰13')
searchbox.send_keys(Keys.ENTER)
time.sleep(3)

# 스크롤 내리기
before_h = driver.execute_script('return window.scrollY')
while True:
    driver.find_element(By.CSS_SELECTOR, 'body').send_keys(Keys.END)
    time.sleep(1)
    after_h = driver.execute_script('return window.scrollY')
    if before_h== after_h:
        break
    before_h=after_h
time.sleep(1)

import csv
f = open('아이폰조사.csv', 'w', newline='')
csvfile = csv.writer(f)


#상품 정보 찾기
elms = driver.find_elements(By.CSS_SELECTOR, 'div.basicList_info_area__TWvzp')
for i in elms:
    name = i.find_element(By.CSS_SELECTOR, 'div.basicList_title__VfX3c').text
    price = i.find_element(By.CSS_SELECTOR, 'span.price_num__S2p_v').text
    link = i.find_element(By.CSS_SELECTOR, 'a.basicList_link__JLQJf').get_attribute['href']
    print(name, price, link)
    csvfile.writerow([name, price])

f.close()     # 파일 닫기
driver.quit() # 크롬 닫기