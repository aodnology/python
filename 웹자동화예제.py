# 셀레니움 기본 설정
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