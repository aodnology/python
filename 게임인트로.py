while True:
    print('메뉴를 입력하세요 : ')
    menu = int(input('1. 게임시작 2. 랭킹보기 3. 게임종료'))
    if menu == 1:
        print('게임시작')
    elif menu == 2:
        print('랭킹')
    elif menu == 3:
        print('또만나요')
        break
    else:
        print('다시 입력하세요')