from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import datatime
from selenium import webdriver
import time

def bean_store(result):
    url ="https://www.coffeebeankorea.com/store/store.asp" #url
    wd = webdriver.Chrome('./webdriver/chromedriver.exe') # driver 사용

    for i in range (1, 400):
        wd.get(url)
        time.sleep(1)
        try:
            wd.execute_script('javascript:storePop2(%d)'%i)
            time.sleep(1)
            html = wd.page_source
            soupCB = Beautifulsoup(html, 'html.parser')
            store_name_h2 = soupCB.select("div.store_txt > h2")