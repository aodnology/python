# O(n^2) : 이차 시간 (Quadratic Time)
# 2차 시간은 중첩 반복(루프안에 루프)이 있을때 발생한다.
# 인풋이 10개 라면 완성하는데 100번의 스텝이 필요한 경우

def print_twice(arr):
    for n in arr:
        for x in arr:
            print(x, n)

