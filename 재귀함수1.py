# def function(k,n):
#     if n == k:
#         return
#     else:
#         function(k+1, n)

# function(0,2)

# # 재귀함수 활용
# def countdown(i):
#     if i == 0:
#         print('투하!')
#     else:
#         print(i)
#         countdown(i-1)

# countdown(4)

# # 위 예제 for문으로 구현하기
# for i in range(5):
#     print(i.sort(reverse=True)) #내림차순
#     if i==0:
#         print('투하')

# 재귀 함수를 사용하여 홀수, 짝수 구분하기
# def jjakhol(a):
#     a = int(a)
#     a >= 0
#     if a % 2 == 0:
#         str(print(a,'= even'))
#     elif a % 2 == 1:
#         str(print(a,'= odd'))
#     jjakhol((a-1))
# jjakhol(50) # 정해진 값(50)이 아닌 50부터 음수까지 표현 되는 결과(실패)

# 재귀 함수 사용 홀수 짝수 구분하기 2

def jjak_hol(b):
    if b % 2 == 0:
        print(b, '= even')
    else :
        print(b, '= odd')

jjak_hol(50)
jjak_hol(49)