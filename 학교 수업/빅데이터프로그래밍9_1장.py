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

# DataFrame 통계적 개요 확인
df.describe()

# 컬럼을 지정하여 정렬
df.sort_values(by='B', ascending=False)
# by 로 지정된 컬럼을 기준으로 정렬한다

# A에 해당하는 컬럼만 Series로 보기
df['A']

# 범위를 지정하여 Series로 보기
df[0:3]

# 행 기준으로 확인하기
df['20220202':'20220203']
#데이터의 행값을 직접 지정한다.

# loc(location) 옵션으로 슬라이싱 하기
df.loc[dates[0]] # 날짜 데이터
df.loc[:,['A', 'B']] # A와 B열의 모든 행 확인
#     [행,[   열   ]]
df.loc['20220202':'20220203',['A','B']] #loc[] 행과 열범위 지정

#2022년 2월 2일의 A,B 컬럼의 내용 확인
df.loc['20220202',['A','B']]

#dates[0] == 2022년 2월 2일에 A 컬럼의 데이터만 확인
df.loc[dates[0],'A']

# iloc를 활용하여 4번 행의 데이터 모두 확인하기
df.iloc[3] # 인덱스와 같이 0번부터 시작

# iloc를 활용하여 4~5행 0~1열 데이터 조회
df.iloc[3:5,0:2]

# 콤마를 지정하여 데이터 가져오기
df.iloc[[1,2,4],[0,2]]
#1,2,4열 0,2행에 포함된 데이터
#print(df.iloc[[1,2,4],[0,2]])

# 열과 행 전체를 가져오고 싶은 경우
df.iloc[1:3,:] # 열 지정, 행 전체
df.iloc[:,1:3] # 행 지정, 열 전체

# 특정 조건을 만족하는 데이터만 가져오기
df[df.A > 0] # 컬럼 A에서 0보다 큰 행만 얻을 수 있음

# 원본 데이터를 유지하고 데이터 복사하기
df2 = df.copy()

# 복사한 DataFrame에 새로운 컬럼 추가
df2['E'] = ['one','two','three','four','three']

# df2['E'] 컬럼에 two, four 유무 확인
df2['E'].isin(['two','four'])
