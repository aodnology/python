#함수나 변수를 모아 놓은 파일
import random
def makelotto():
    lotto=[]
    while true:
        num = random.randint(1,45) # 1~45중에 임의의 숫자를 선택
        if num in lotto:
            continue
        lotto.append(num)
        if len(lotto)==6:
            break
    return lotto
print(lotto)