# 태어난 연도를 입력받으면, 현재 나이를 출력하기

year = int(input('태어난 연도 : '))
# x = (input('태어난 연도 : '))
# x = int(x)

#datatype을 확인 하는 변수
type(year)

age = 2022-year+1
print(str(age)+'살입니다.')
print(age, '살입니다.')
# 변수들을 이어서 출력하고자 할때 , + 를 사용할 수 있다. 콤마(,)로 연결하는 경우는 공백이 생긴다.1

if age > 20:
    print('축하합니다')
print('종료합니다')