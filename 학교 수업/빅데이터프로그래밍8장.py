import urllib.request # 웹의 특정 주소로 요청을 보내는 기능
import bs4            # 데이터 파싱을 위해 뷰티솝에 파이썬에서 가공할 수 있는 형태로
url = "https://www.naver.com"
html = urllib.request.urlopen(url) # <html></html> 웹페이지를 불러옴

bs_obj = bs4.BeautifulSoup(html, "html.parser") # 파싱데이터 가공

# <div> 태그 중 class가 service_area인 첫번째로 나오는 div 태그 찾기
top_right = bs_obj.find("div", {"class":"service_area"})

# <a> 안에 있는 text만 뽑기
first_a = top_right.find("a") 

