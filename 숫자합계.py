# 0부터 입력된 숫자까지의 합계를 출력하는 예제
total = 0
num = int(input('숫자를 입력하시오 : '))
for i in range(1, num+1):
    total = total + i
print(total)