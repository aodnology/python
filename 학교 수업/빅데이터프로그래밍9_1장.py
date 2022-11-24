import pandas as pd # as [별명]
import numpy as np

# 데이터 생성
s = pd.Series([1,3,5,np.nan,6,8])
'''
Pandas에서 Series란? 
(
Series는 어떤 데이터 타입이든 보유할 수 있는 레이블(label)링된 1차원 배열
//레이블링이란 주어진 데이터에 정답지를 만들어주는 작업이고, 이때 정답지를 레이블이라한다.
)

NaN (결측값) 이란?
(
Not a Number의 약어
표현 불가능한 수치형 결과를 의미함.
)
'''

dates = pd.date_range('20220202', periods=6)
print(dates)