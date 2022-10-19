# # 그리디 알고리즘은 매 순간 가장 좋아보이는 것만 선택하며, 
# # 현재의 선택이 나중에 미칠 영향에 대해서는 고려하지 않는다.
# # 총 동전의 수 return

money = int(input("액수를 입력하세요 : "))
coin_types = [500, 100, 50, 10]
count = 0
for coin in coin_types:
    count += money // coin
    money %= coin

print(count)

# 큰 단위의 화폐부터 차례대로 확인하기