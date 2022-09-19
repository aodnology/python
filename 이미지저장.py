from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager #크롬 드라이버 자동 업데이트
import time

query = input('수집할 이미지 : ')

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

driver.get('https://www.google.co.kr/search?q='+query+'&hl=ko&tbm=isch&source=hp&biw=896&bih=1018&ei=mRv-YunkDKCB1e8Pq9Cc0AY&iflsig=AJiK0e8AAAAAYv4pqZFcU5DHluZyaqTizTcLFLvNvlGw&ved=0ahUKEwiplfqEntD5AhWgQPUHHSsoB2oQ4dUDCAc&uact=5&oq=%EA%B3%A0%EC%96%91%EC%9D%B4&gs_lcp=CgNpbWcQAzIICAAQgAQQsQMyCwgAEIAEELEDEIMBMggIABCABBCxAzIICAAQgAQQsQMyCAgAEIAEELEDMggIABCABBCxAzIICAAQgAQQsQMyCAgAEIAEELEDMgQIABADMggIABCABBCxAzoFCAAQgAQ6CAgAELEDEIMBUO4FWKYUYIQWaAJwAHgBgAF2iAHwBpIBAzYuM5gBAKABAaoBC2d3cy13aXotaW1nsAEA&sclient=img#imgrc=YzKqurAoZRMdsM')
driver.implicitly_wait(7)

#저장 함수
from urllib.request import urlretrieve

#폴더 생성
import os
os.makedirs(os.getcwd()+'/'+query)
#              현재폴더위치     폴더명
elems = driver.find_elements(By.CSS_SELECTOR, 'img.rg_i.Q4LuWd')
count = 1
for e in elems:
    e.click()
    time.sleep(3)
    try:
        img_info = driver.find_element(By.CSS_SELECTOR, 'img.n3VNCb.KAlRDb')
        imglink = img_info.get_attribute('src')
        print(imglink)
        filename = './'+query+'/'+str(count)+'.jpg'
        urlretrieve(imglink, filename)
        count=count+1
    except:
        # continue
        print('pass')

driver.quit()
