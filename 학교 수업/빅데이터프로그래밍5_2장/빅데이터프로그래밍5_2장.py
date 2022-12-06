print('1. 모듈')
# 모듈 : [함수]나 [변수] 또는 [클래스]를 [모아 놓은 파일]
# 다른 파이썬 프로그램에서 불러와 사용할 수 있게 만들어진 파이썬 파일이라고 할 수 있음

import mod1 # 모듈 불러오기
from mod1 import sum, safe_sum # 모듈 내에 함수 불러오기 

print('2. 클래스나 변수 등을 포함한 모듈 mod2.py 참고')

from mod2 import Math , sum
import mod2
a = Math()
print(a.solv(2))
print(mod2.Pl) # mod2 안에 변수값 가져오기
print(mod2.sum(mod2.Pl, 4.4))
