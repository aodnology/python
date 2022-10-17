# 리스트 자료형
# 변수 = [ 요소1, 요소2, 요소3, ]

a = []
b = [1,2,3]                     #숫자
c = ['life','is','too','short'] #문자열
d = [1,2,'life','is']           #숫자, 문자열
e = [1,2,['life','is']]         #숫자, 리스트 구조로 사용 가능

print('1. ')
# 리스트의 인덱싱과 슬라이싱
#    0 1 2  : 인덱싱 번호
a = [1,2,3]
print(a)
print(a[0])
print(a[0]+a[2]) # 리스트 a의 인덱싱 0번 + 2번
print(a[-1])     # 리스트 a의 마지막 요소값 : '-'를 붙이면 뒤에서 부터 요소값을 메김

print('1-2. ')
a = [1, 2, 3, ['a','b','c']]
print(a[-1], a[3])

print('2. ')
#리스트 a에서 포함된 ['a','b','c']라는 리스트에서 값들을 인덱싱하는 방법
print(a[-1][0], a[-1][1], a[-1][2])
#리스트 안에 리스트가 선언된경우 변수[리스트인덱스번호][리스트안의인덱스번호]

#a[-1][0] : a
#a[-1][1] : b
#a[-1][2] : c

print('3. ')
#리스트의 슬라이싱
#변수[ 시작인덱스 : 마지막인덱스 ] ( 마지막인덱스번호는 포함하지 않고 슬라이싱 함 )
a = [1,2,3,4,5]
print(a[0:2])   # 결과 : [1,2]
print(a[:2])    # 2번 인덱스를 포함하지 않고 출력
print(a[2:])    # 2번 인덱스를 포함하여 출력
#시작 기준 : 포함 , 마지막 기준 : 비포함

print('4. ')
#리스트 연산자
a = [1,2,3]
b = [4,5,6]
print(a + b) # [1,2,3,4,5,6] : 리스트 요소끼리의 합이 아니라 말그대로 두개의 리스트가 하나로 통합 됨

print('5. ')
#리스트 반복하기 (*)
a = [1,2,3]
print(a * 3) # 리스트가 세번 반복됨

print('6. ')
#리스트 데이터 타입 일체화
a = [1,2,3]
# a[2] + "hi" : 수행 불가
# 숫자와 문자열을 합치려할때 데이터 타입이 같지 않기 때문에 오류가 발생함
# a[2]+ "hi" (3hi) 출력방법

print(str(a[2])+"hi") # str(변수)+"문자열"
                      # type

print('7. ')
#리스트의 수정, 변경과 삭제
#1. 하나의 값 수정
a = [1,2,3]
a[2] = 4    #인덱스 2번의 값이 4로 변경 : [1,2,4]
print(a)

print('7-2. ')
#리스트에서 연속된 범위의 값 수정
a[1:2] # 2
a[1:2] = ['a','b','c'] # 인덱스번호 1부터 2번전까지 슬라이싱된 형태로 리스트가 대입되면 리스트안에 해당 인덱스번호(1)위치에 대입됨
#a[2] = ['a','b','c']  # 슬라이싱을 하지 않고 인덱스 번호에 리스트를 대입하면 리스트안에 리스트가 대입되는 형태가 됨
print(a)

print('8. ')
#리스트 요소 삭제
a = [1,'a','b','c',4]
a[1:3]=[] # [1:3] 인덱스번호 1,2요소 삭제
print(a)

print('8-2. ')
del a[1] # 인덱스번호 1번 요소 삭제(del)
print(a)

print('9. ')
# 요소 추가append
a = [1,2,3]
a.append(4)
print(a)
a.append([5,6]) # 리스트 안에는 어떤 자료형도 추가 가능
print(a)

print('10. ')
#리스트 정렬(sort)
a = [1,4,3,2]
a.sort()
print(a)

a = ['a','c','b']
a.sort()
print(a)

print('11. ')
a.reverse() # 리스트를 역순으로 뒤집음
print(a)

print('12. ')
# 위치반환 index()
a = [1,2,3]
print(a.index(3)) # 인덱스 번호가 반환됨 (2)
print(a.index(1))

print('13. ')
# 요소삽입 insert()
a = [1,2,3]
a.insert(0,4) # 인덱스번호 0번에 숫자 4추가
print(a)
a.insert(3,5) # 인덱스번호 3번에 숫자 5추가
print(a)

print('14. ')
# 리스트 요소 제거 remove()
a = [1,2,3,1,2,3]
a.remove(3)
print(a) # 리스트안에 같은 값이 있을 경우 빠른순번 인덱스번호의 값이 삭제된다

print('15. ')
# 리스트 요소 끄집어내기 pop()
a =[1,2,3]
print(a.pop()) 
# ()안에 아무값도 넣지 않을경우 마지막 값을 끄집어내고 삭제함
# ()안에 숫자를 입력하면 해당하는 인덱스 번호의 값을 끄집어내고 삭제함
print(a)

print('16. ')
# 리스트에 포함된 요소 x의 개수 세기 count()
a = [1,2,3,1]
a.count(1)
print(a)

print('17. ')
# 리스트확장 extend()
a = [1,2,3]
a.extend([4,5])
# extend(x)의 값은 무조건 리스트만 올 수 있으며 기존의 리스트와 입력된 리스트가 합해진다
print(a)

b = [6,7]
a.extend(b)
print(a)

print('18. ')
#튜플 (tuple)
#튜플은 요소값 수정 ,삭제 및 변경이 불가능
t1 = (1, 2, 'a','b')
t2 = (3, 4)

print('18-2. ')
#튜플 연산
th = t1+t2
print(th)     # (1,2,'a','b',3,4)
print(t2 * 3) # (3,4,3,4,3,4)

print('18-3. ')
#튜플 인덱싱
t1 = (1,2,'a','b')
print(t1[0])
print(t1[3])

#튜플 슬라이싱
t1 = (1,2,'a','b')
print(t1[1:])

print('19. ')
#딕셔너리 자료형 {}
#java collection framework의 Map과 같이 key, value 값을 가진다

dic = {'name' : 'sooho', 'phone' : '112', 'birth' : '05/23'}
print(dic['name'])
print(dic['phone'])

a = {3:'three', 2:'two', 1 :'one'}
del a[2] # []안에 입력된 key : value값이 삭제된다.
print(a)

#딕셔너리 key값 가져오기
print(a[1])
print(a.get(1))
# a[x]와 a.get(x)의 결과값 모두 x에 해당하는 value 값을 가져온다
# 차이점
# a[x]의 경우 x에 해당하는 key값이 없는 경우 오류가 발생
# a.get(x)의 경우 x에 해당하는 key값이 없는 경우 None을 return

print('20. ')
#딕셔너리 관련함수
a = {'교수' : '김영운', '과목' : '파이썬', '수업요일' : '수요일'}

# keys() : key 리스트를 생성
# 변수.keys()
print(a.keys())

# dict_keys 객체는 리스트 고유함수 사용 불가능
# 리스트 고유 함수 : append(), insert(), pop(), remove(), sort()

# values() : value 리스트 생성
print(a.values())

for k in a.values():
    print(k)

# items() : 딕셔너리 자료 key, value 모두 얻기
print(a.items()) # 튜플로 묶은 값을 dict_items 객체로 돌려줌

# clear() : 딕셔너리 모두 지우기
a.clear()
print(a)

# in : 딕셔너리에서 키 존재하는지 확인하기
# 키이름 in 딕셔너리변수
a = {'1' : 'one', '2': 'two', '3':'three'}
print('1' in a)

print('21. ')
# 집합 자료형 set()
# 특징 : 중복, 순서 X
# 순서가 없기 때문에 인덱싱으로 값을 얻을 수 없음. 인덱싱으로 접근하려면 리스트나 튜플로 변환 해야함
s1 = set("hello") 
print(s1)           # 문자열에 ll이 있는데 중복이 되지 않으므로, l만 출력

s1 = set([1,2,3])
l1 = list(s1)       # 집합자료형을 리스트 자료형으로 변환
print(l1)

print('22. ')
# 집합 자료형 set()응용 
# 교집합 &
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])

print(s1 & s2)
#s1.intersection(s2) 위 코드와 동일한 결과

# 합집합 |
print(s1 | s2)
#s1.union(s2) 위 코드와 동일한 결과

# 차집합 -
print(s1 - s2) # s1을 기준으로 값이 정해짐
print(s2 - s1) # s2를 기준으로 값이 정해짐

# add() : 집합 자료형에 값 한 개 추가
s1 = set([1,2,3])
s1.add(4)
print(s1)

# update() : 집합 자료형에 값 여러개 추가
s1.update([4,5,6,7])
print(s1)

# 특정 값 제거하기(remove)
s1 = set([1,2,3])
s1.remove(3)
print(s1)

print('23. ')
# 자료형의 참과 거짓
# 숫자형
# true : 0, false : 1
# 나머지 자료형
# true : 값 존재 할 때, false : 값이 존재하지 않을 때

a = [1,2,3,4]
while a :
    print(a.pop()) # pop() : 요소를 끄집어내는 함수

if set([]):
    print("True")
else:
    print("False")

if {1 : 'one', 2 : 'two', 3 : 'three'}:
    print("True")
else:
    print("False")

print('24. ')
# 변수를 만드는 여러가지 방법

a, b = ('park', 'sooho')
print(a) # park
print(b) # sooho

(a, b) = '박', '수호' # 튜플은 괄호를 생략해도됨
print(a) # 박
print(b) # 수호

[a, b] = ['python', 'life']
print(a, b)

a = b = 'park'
print(a)
print(b)
print(a,b)

print('25. ')
# 변수의 값 바꾸기
a = 3
b = 5
a, b = b, a
print(a) # 5
print(b) # 3

print('26. ')
# del(변수) : 메모리에 생성된 변수 없애기 
a = 7
b = 9
print(a,b)

del(a)
#print(a) 오류 출력

print('27. ')
# 리스트를 변수에 넣고 복사
a = [1,2,3,4]
b = a       # b와 a가 같은 리스트인 [1,2,3,4]를 가리키는 상태
a.append(5) # 변화가 두개의 변수에 같이 적용됨
print(b)

a[1]
print(b)