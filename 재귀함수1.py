# def function(k,n):
#     if n == k:
#         return
#     else:
#         function(k+1, n)

# function(0,2)

#
def countdown(i):
    if i == 0:
        print('투하!')
    else:
        print(i)
        countdown(i-1)

countdown(4)

#
for i in range(5):
    print(i.sort(reverse=True)) #내림차순
    if i==0:
        print('투하')


# def jjakhol(a):
#     a = int(a)
#     a >= 0
#     if a % 2 == 0:
#         str(print(a,'= even'))
#     elif a % 2 == 1:
#         str(print(a,'= odd'))
#     jjakhol((a-1))
# jjakhol(50)