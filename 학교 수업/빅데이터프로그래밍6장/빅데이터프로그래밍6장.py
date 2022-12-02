# 함수 이용하기

def gugu(n): 
    result = []             
    i = 1
    while i <10:
        result.append(n * i)
        i += 1
    return result

''' 
3 : 함수 선언
4 : result 변수명의 리스트 자료형 생성
5 : 1~9까지 대입할 변수[i] 선언
6 : i < 10 으로 9단 까지 반복
7 : 리스트 자료형에 append() 함수를 활용하여 값 추가
8 : i 1씩 증가
9 : 구구단 값이 담기는 리스트 자료형 변수에 결과값 넣기
'''
print(gugu(2))

# 3과 5의 배수 더하기
hap = 0
for i in range(1, 100):
    if i % 3 == 0 or i % 5 == 0:
        hap += i
print(hap)

#게시판 페이징하기
'''
게시물의 총 건수와 페이지에 보여줄 게시물 수를 입력으로 주었을 때
총 페이지수를 출력하는 프로그램
'''
def getTotalPage(m,n):
    if m % n == 0:
        return m // n
    else :
        return m // n + 1

'''
34 : m == 게시물의 총 건수
     n == 페이지당 보여줄 게시물 수
     총 페이지수 = 총 건수 / 한 페이지당 보여줄 건수 + 1
'''
# print(getTotalPage(5,10))
# print(getTotalPage(15,10))
# print(getTotalPage(25,10))
# print(getTotalPage(35,10))

# 메모장
