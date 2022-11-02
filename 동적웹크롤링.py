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
            store_name = store_name_h2[0].string
            print(store_name)
            store_info = soupDB.select("div.store_txt > table.store_table > tbody > tr > td")
            store_address_list = list(store_info[2])
            store_address = store_address_list[0]
            store_phone = store_info[3].string
            result.append([store_name]+[store_address]+[store_phone])
        except:
            continue
    return

def main():
    result = []
    print("coffee bean crawling")
    bean_store(result)

    CB_tb1 = pd.DataFrame(result, columns=('store', 'address', 'phone'))
    CB_tb1.to_csv('./CoffeeBean.csv', encoding='cp949',mode='w', index=True)

if __name__ == '__main__':
    main()