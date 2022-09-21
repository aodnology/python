# for문 기본 구조
#
# for 변수 in 리스트[](또는 튜플(), 문자열):
#     수행할 문장1
#     수행할 문장2

#기본형
list = ['one', 'two', 'three']
for i in list: # list안에 요소들이 순차적으로 i에 대입된다.
    print(i)   # i에 대입된 list요소들 출력

#리스트 튜플 자료형
a = [(1,2), (3,4), (5,6)]  # [] : 리스트 자료형 , () : 튜플 자료형
for (first, last) in a:    # 리스트의 요솟값이 튜플이기 때문에 각각의 요소 자동으로 (first, last) 변수에 대입 된다.
    print(first + last)

b = [('안녕','하세요'), ('히사','시부리')]
for (앞머리, 말머리)in b:
    print(앞머리+말머리)

#응용형 : 성적으로 합격 불합격 나누기
marks = [90,25,67,45,80]

number = 0 # 학생을 넘버링 하기 위해 변수 선언
for mark in marks:
    number = number +1
    if mark >= 60:
        print("%d번 학생은 합격입니다." %number)
    else:
        print("%d번 학생은 불합격입니다." %number)