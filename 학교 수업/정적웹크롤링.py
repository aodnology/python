from unittest import result
from bs4 import BeautifulSoup
import urllib.request
import pandas as pd

def hollys_store(result):
    for page in range(1, 55):
        url = 'https://www.hollys.co.kr/store/korea/korStore.do?pageNo=%d&sido=&gugun=&store=' %page
        print(url)
        html = urllib.request.urlopen(url)
        soupHolly = BeautifulSoup(html, 'html.parser')
        tag_tbody = soupHolly.find('tbody')
        for store in tag_tbody.find_all('tr'):
            if len(store) <= 3:
                break
            store_td = store.find_all('td')
            store_name = store_td[1].string
            store_sido = store_td[0].string
            store_address = store_td[3].string
            store_phone = store_td[5].string
            result.append([store_name]+[store_sido]+[store_address]+[store_phone])
        return

def main():
    result = []
    print('hollys store crawling ==>')
    hollys_store(result)
    hollys_tbl = pd.DataFrame(result, columns=('store','sido-gu','address','phone'))
    hollys_tbl.to_csv('./hollys.csv',encoding='cp949', mode='w', index=True)
    print(result)
    del result[:]

if __name__ == '__main__':
    main()