# 출석률 계산 프로그램 만들기

from unittest import result


def makerate(m, a):
    result = a/m * 100
    return result

# 1회차 출석률
output = makerate(15, 13)
print(output)
# member = 15
# attendence = 13
# rate = attendence/member *100
# print(rate)

# 2회
output = makerate(20, 8)
print(output)
