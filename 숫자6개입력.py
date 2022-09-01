#append == list가 만들어져있는 상태에서 추가 가능
lotto = [] # [] == list를 만든 형태

for num in range(6): #6번 반복하겠다는 의미
    num = input('숫자를 입력하시오 : ')
    num = int(num)
    lotto.append(num) # 입력한 숫자를 리스트에 추가 / 변수.append(입력값을 담는 변수)

print(lotto)