print('1. 함수')
# def : 함수
#
# def 함수명(입력인수):
#    <수행할문장>
#    <수행할문장2>
#    ...
#   return 결과값
print('1-2. 함수 사용의 예')
def sum(a,b):
    return a + b
a = 3
b = 4
c = sum(a,b) #return값을 c에 대입
print(c)

print('1-3. 함수의 전형적인 예')
def sum(a,b):
    res = a+b
    return res
c = sum(5,9)
#결과값을 담을 변수(c) = 함수명(입력인수1, 입력인수2)
print(c)

print('2. 입력 값이 없는 함수')
def say():
    return 'hi'
a = say()
print(a)

print('2-2. 결과 값이 없는 함수')
def sum(a, b):
    print("%d, %d의 합은 %d입니다"%(a,b,(a+b)))
sum(5,4)
a = sum(5,4)
print(a) # return 값이 없으므로 결과값이 없음

print('2-3. 입력값도 결과값도 없는 함수')
def say():
    print('hi')
say()

print('2-4. 입력값이 몇개가 될지 모를때의 함수 사용의 예')
# def 함수명(*입력 변수)
#     수행할문장
#     ...

def sum_many(*num): # *변수명 : 입력 된 값을 전부 모아서 튜플로 만들어줌
    sum = 0
    for i in num:
        sum = sum + i
    return sum

a = sum_many(1,2,3,4,5,6,7,8,9,10) # 함수 생성시 *입력변수 형태로 작성하여 가능해진 형태
print(a)


def sum_many(choice, *args):
    if choice == 'sum':
        res = 0
        for i in args:
            res += i
    elif choice =='mul':
        res = 1
        for i in args:
            res *= i
    return res

r = sum_many('mul', 1,2,3,4,5)
print(r)

print('3-1. 함수의 리턴값은 언제나 하나')

def sum_and_mul(a,b):
    return a+b,a*b

a = sum_and_mul(3,4)
print(a)

asum, bmul = sum_and_mul(3,4) #튜플 값으로 결과를 돌려받음
print(asum, bmul)             #각각의 결과 값을 받고 싶을때 : 변수, 변수2 = 함수(요소,요소)

print('3-2. 함수안에 리턴 값을 두개 사용하는 경우')

def sum_and_mul(a,b):
    return a+b
    return a*b

r = sum_and_mul(3,4)
print(r)             # 첫번째 return문에 대한 결과값난 돌려준 다음 함수를 빠져나옴

print('3-3. return 활용')
# 특별한 상황에서 함수에서 빠져나오고 싶을때 사용하기

def nick(nick):
    if nick == '바보':
        return
    print("나의 별명은 %s" %nick)

nick('호호')
nick('바보')

print('4. 입력인수 초기값 미리 설정하기')
# 인수=True

def myself(name, old, man=True): # 초기화시키고 싶은 입력변수(man)는 항상 마지막에 작성
    print('이름 : %s' %name)
    print('나이 : %s' %old)
    if man:
        print('남자')
    else:
        print('여자')
    return name,old,man

a = myself('박수호',32,)

print('5. 함수 안에서 선언된 변수의 효력 범위')
a = 1
def test(a):
    a += 1
    print(a) # 같은 변수를 사용했으나 함수 안에서만 사용되는 변수 결과적으로 서로 다름
print(a)     # 같은 변수를 사용했으나 함수 밖에서만 사용되는 변수 결과적으로 서로 다름

b = 1
def vartest(b):
    b += 1
    return b
b = vartest(b)  # test(b)를 b 변수에 대힙하여 값을 가져오나 여기서도 함수 안의 b 변수는 함수 밖의 b와 다름
print(b)

print('5-2. global 명령어 사용하여 함수 밖의 변수 직접 사용하기')
a=1
def vertest_global():
    global a
    a += 1

vertest_global()
print(a)

print('6. input() : 사용자 입력')

# num = input('숫자를 입력하세요 : ')
# print("입력된 숫자: "+num)

print("7. print() : 출력 자세히 알기")

print('1.',"life""is""too short")   # 문자열 이어쓰기 (")
print('2.',"life"+"is"+"too short") # 문자열 이어쓰기 (+)
print('3.',"life","is","too short") # 문자열 띄어쓰기 (,)

print("7-2. 한줄에 결과값 출력하기")

for i in range(10):
    print(i, end=" ")

print("8. open() : 파일 생성하기")
# 새로운 파일로 생성 : 파일생성하기.py 참조

