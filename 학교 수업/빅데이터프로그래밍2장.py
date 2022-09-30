print('1.')
# .real : 복소수 실수 부분 반환 

a = 1 + 2j # 대문자도 사용가능
print(a.real)     # .real == 복소수 변수의 실수 부분을 반환

print('2.')
# .imag : 복소수의 허수 부분을 반환
a = 1 + 2j
print(a.imag)

print('3. ')
# 사칙연산
a = 2
b = 5
print('3-1. ', a + b)
print('3-2. ', a * b)
print('3-3. ', a / b)
print('3-4. ', a ** b)        # 제곱 (3^4)
print('3-5. ', a % b, b % a)  # 나머지
print('3-6. ', a // b)        # 소수점 아랫자리 버림

print('4. ')
# 믄지열
# 작은따옴표(') 안에 큰따옴표(") : 문자열을 나타내기 위한 기호로 인식
# 큰따옴표(") 안에 작은따옴표(') : 기호로 인식하지 않음

food = "박수호's" 
print("4-1 ", food)
say = '"박수호"'+"'s"
print("4-2 ", say)

print("5. ")
#여러 줄인 물자열을 변수에 대입하고 싶을 때
# 큰따옴표(") 3개로도 사용 가능

multiline ='''
안녕하세요
반갑습니다
파이썬공부중입니다
'''
print(multiline)

print('6. ')
# 문자열 더해서 연결하기

head = 'python'
tail = " is fun"
print(head+tail)

print('7. ')
# 문자열 곱하기
a = 'python'
print(a * 4)

print('7-2. ')
#문자열 곱하기 응용

print("=" * 50); print("my program"); print("="*50)
# print문 여러개를 한줄로 사용할때는 세미콜론(;)을 찍어사용가능

print('8. ')
# 문자열 인덱싱과 슬라이싱
# 인덱싱 : 무엇인가를 가리킴
# 슬라이싱 : 무언인가를 잘라냄

a = "Life is too short, You need Python"
print(a[0],a[-0],a[3],a[-1]) # 변수[-n] : 뒤에서 n번째 문자를 가져옴 , 인덱싱 활용 예제

print('8-2. ')
# 단어 뽑아내기
# 슬라이싱 활용 예제

print(a[0:4], a[5:7], a[12:17]) # 변수[시작번호:끝번호] , 결과 : Life
print(a[19:]) # 끝번호를 생략하면 시작 인덱싱 번호부터 문자열을 끝까지 뽑아냄
print(a[:17]) # 시작번호를 생략하면 처음부터 끝 번호가지 뽑아냄
print(a[:]) # 시작번호와 끝번호가 없으면 print(a)와 결과가 같음 

print('8-3. ')
#슬라이싱으로 문자열 나누기

a = "20010331Rainy"
date = a[:8]        # a[8] 포함 X
weather = a[8:]     # a[8] 포함 O
print(date, weather)

