coffee = 10 # 커피의 총량
while True:
    money = int(input("돈을 넣어주세요: "))
    if money == 300:
        print('커피가 나옵니다.')
        coffee = coffee -1
    elif money > 300:
        print('거스름돈 %d원과 커피 나옵니다.'%(money-300))
        coffee = coffee - 1
    else:
        print("돈을 다시 돌려주고 커피를 주지 않습니다.")
    if not coffee:
        print('커피가 다 떨어졌습니다.')
        break
    print("남은 커피의 양은 %d개 입니다."%coffee)

# print('2-3. ')
# # 금액이 다 할때까지 커피 뽑기

# coffee = 10 # 추출가능한 커피양
# money = int(input("돈을 넣으세요 : ")) #투입금액
# price = 100 #커피 한잔 가격
# while money:
#     print("커피가 나옵니다")
#     coffee = coffee - 1
#     money = money - price
#     print('남은 커피양 : %d개'%coffee)
#     print('남은돈 : %d'%money)
#     if not coffee:
#         print('커피가 다떨어졌습니다')
#         break
#     elif money <= 0:
#         print("돈이 다 떨어졌습니다")
#         break
