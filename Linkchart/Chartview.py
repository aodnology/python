import plotly.graph_objects as go
from plotly.subplots import make_subplots
from pandas_datareader import data  
from datetime import datetime
import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objects as go


# 데이터를 가져올 날짜 설정
start_date = datetime(2020,9,14)
end_date = datetime(2021,9,14)

# 야후에서 삼성전자 데이터 가져오기
samsung = data.get_data_yahoo("005930.ks", start_date, end_date)

samsung = samsung.reset_index() # Date index를 Column으로 보내주기 위함

# plotly 캔들스틱 그래프 그리기
stock_name = '삼성전자'
fig = go.Figure(data=[go.Candlestick(x=samsung['Date'],
                                    open=samsung['Open'],
                                    high=samsung['High'],
                                    low=samsung['Low'],
                                    close=samsung['Close'])])
# x축 type을 카테고리 형으로 설정, 순서를 오름차순으로 날짜순서가 되도록 설정
fig.layout = dict(title=stock_name, 
                       xaxis = dict(type="category", 
                                    categoryorder='category ascending'))
fig.update_xaxes(nticks=5)
fig.show()

start_date = datetime(2020,9,14)
end_date = datetime(2021,9,14)

#카카오
kakao = data.get_data_yahoo("035720.ks", start_date, end_date)

kakao = kakao.reset_index() 

stock_name = '카카오'
fig = go.Figure(data=[go.Candlestick(x=kakao['Date'],
                                    open=kakao['Open'],
                                    high=kakao['High'],
                                    low=kakao['Low'],
                                    close=kakao['Close'])])
fig.layout = dict(title=stock_name, 
                       xaxis = dict(type="category", 
                                    categoryorder='category ascending'))
fig.update_xaxes(nticks=5)
fig.show()