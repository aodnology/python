#1. 변수에 문자 대입하고 출력하기
a = 'python'            # 따옴표 (') 쌍따옴표("")의 차이
print("1. ", a)         # : 'python' == 문법적으로 의미를 가지는 단위의 경우
                        # : "python" == 크게 의미를 가지지 않는 문자열 
                        # 사실 큰 의이 없음

#2. 복소수 지원
a = 2 + 3j
b = 3
print('2. ', a * b) # 콤마(,)는 자바 (+) 의 의미와 같


#3. 조건문(if)
a = 3
if a > 1:
    print("3. ", "a is greater than 1")


#4. 반복문(for)
print('4. ')
for a in [1,2,3]: # 리스트([]) 안의 값을 a 안에 넣어 하나씩 꺼내 사용함
    print(a)


#4-2. 반복문(for) 응용 리스트 문자열 한줄로 춮력
print('4-2. ')
for a in [1,2,3]: # 리스트([]) 안의 값을 a 안에 넣어 하나씩 꺼내 사용함
    print(a, end=' ') # end=''에서 ''안에 특정 값을 입력하면 요소 사이에 그 값이 입력됨


#5. 반복문 while
print('5. ')
i = 0           #초기화
while i < 3:    #조건식
    i = i+1     #증감식 
    print(i)    #과 같은 기본 while문의 구조와 같음


#5-2. 반복문 while
print('5-2.')
i = 0           #초기화
while i < 3:    #조건식
    i = i+1     #증감식 
    print(i, end=' ') #for 반복문과 마찬가지로 end


#6. 함수(def)
def sum(a, b):
    return a+b # a와 b를 더하는 함수를 생성

print('6.', sum(3,4))