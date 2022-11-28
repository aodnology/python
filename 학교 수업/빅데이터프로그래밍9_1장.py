import pandas as pd # as [별명]
import numpy as np

# 데이터 생성
s = pd.Series([1,3,5,np.nan,6,8])
'''
Pandas에서 Series란? 
:
Series는 어떤 데이터 타입이든 보유할 수 있는 레이블(label)링된 1차원 배열
//레이블링이란 주어진 데이터에 정답지를 만들어주는 작업이고, 이때 정답지를 레이블이라한다.


NaN (결측값) 이란?
:
Not a Number의 약어
표현 불가능한 수치형 결과를 의미함.

'''

# 날짜형 데이터 생성
dates = pd.date_range('20220202', periods=6)
print(dates)
'''
data_range() : 날짜형 데이터 함수
periods=[숫자]

2022년2월2일 기준으로, 6일동안의 기간을 dates 변수에 지정함
'''

# Dataframe 유형 데이터 생성
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=['A','B','C','D'])
print(df)
'''
np.random.randn(6,4) : 표준 정규 분포에서 난수 matrix array 생성
index=date : index(행)을 date(앞에 만든 날짜형 데이터) 대입
column=['A','B','C','D'] : 열로 지정
'''

# 데이터 확인
df.head(3)
# print(df.head(3))
# head() 함수를 사용하면 입력된 값 만큼(3)의 정보 확인가능, 기본적으로는 5행 까지 보여줌

# 데이터의 컬럼, 인덱스, 내용 확인
df.index   #컬럼
df.columns #인덱스
df.values  #내용

# DataFrame 개요 확인
df.info()

