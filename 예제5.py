price = input('가격 : ')
price = int(price)

if price >= 50000:
    print('매도합니다')
elif price >= 30000:
    print('대기중입니다')
else:
    print('매수합니다')

