# 프로그램 구조 제어문

print('1. if')
# if

#돈이 있으면 택시를 타고 없으면 걸어가는 프로그램
money = 1
if money:
    print("택시")
else:
    print("걸어가시오.")

print('1-2. ')
# 3000원 이상의 돈이나 카드가 있으면 택시를 타고 없으면 걸어가는 프로그램

money = 2000
card = 1
if money>=3000 or card:
    print('택시')
else :
    print("걸어가시오.")


print('1-3. ')
# 주머니에 돈이 있으면 텍시를 타고, 없으면 걸어가라
pocket = ['dream','hand','wallet','money']
if 'money' in pocket: # 요소 in 리스트
    print("택시")
else:
    print("걸어가시오.")


print('1-4. ')
# pass : 특정조건에서 아무 일도 하지 않게 설정하기
pocket = ['dream','hand','wallet','money']
if 'money' in pocket:
    pass
else:
    print("걸어가시오.")


print('2. while')
# while
# 10번찍어서 넘어가는 나무 프로그램

treehit = 0
while treehit < 10:
    treehit = treehit + 1
#    print('나무를',treehit,'번 찍었습니다')
    print('나무를 %d번 찍었습니다.' %treehit)
    if treehit == 10:
        print('넘어갔습니다.')

print('2-2. ')
# break : while문 강제로 빠져나가기
coffee = 10
money = 300
while money:
    print("커피가 나옵니다.")
    coffee = coffee - 1
    print('남은 커피의 양은 %d개 입니다.' %coffee)
    if not coffee:
        print("커피가 다 떨어졌습니다")
        break


print('2-3. ')
# continue : 조건이 맞지 않아도 반복문 이어가기

a = 0
while a < 10:
    a = a + 1
    if a % 2 == 0: 
        continue
    print(a)


# print('2-4. ')
# # while True: :무한루프
# while True:
#     print('종료하려면 ctrl+c를 누르세요')

print('3. for')
# for문의 기본 구조

# for 변수명 in 변수:(리스트, 튜플, 문자열)
#   수행할 내용
#   수행할 내용2

list = [1,2,3]
for i in list :
    print(i)

print('3-2. ')
a = [(1,2),(3,4),(5,6)]
for (first, last) in a: # for의 변수명을 변수의 자료형과 같게한다.
    print(first + last)

print('3-3. ')
#for 활용 구구단

for i in range(2,10):
    for j in range(1,11):
        print("%d * %d = %d"%(i,j,(i*j)),end=" ")
    print('') # j의 모든 값 대입이 끝나면 열 바꾸기

print('3-4. ')
#append() 사용 리스트 안에 for문 포함하기

a = [1,2,3,4]
res = [aa * 3 for aa in a]
print(res)

# print('풀이')
#
# a = [1,2,3,4]
# res =[]
# for aa in a:
#     res.append(aa*3)
# print(res)
#

print('3-5. ')
# 짝수에만 3 곱하기

a = [1,2,3,4]
res = [num * 3 for num in a if num % 2 == 0]
#     [연산식    for문        if문            ]
print(res)
# for num in a:
#     if num % 2 == 0:
#         res.append(num*3)
# print(res)

print('3-6. ')
#리스트 반복문 활용 구구단
res = [i*j for i in range(2,10) for j in range(1,10)]
print(res)