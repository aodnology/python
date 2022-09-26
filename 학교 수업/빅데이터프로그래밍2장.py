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

print('7-1. ')
#문자열 곱하기 응용

print("=" * 50); print("my program"); print("="*50) 
# print문 여러개를 한줄로 사용할때는 세미콜론(;)을 찍어사용가능