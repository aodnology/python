coffee = int(input('커피 가격 : '))
cake = int(input('케잌 가격 : '))
result = coffee+cake
if result > 19999:
    price = result * 0.8
    print('20% 할인')
elif result > 9999:
    price = result * 0.85
    print('15% 할인')
else:
    price = result * 0.9
    print('10% 할인')

print(price) # 출력 된 결과물을 통해 price가 float 데이터 타입임을 알 수 있다.
print(int(price))