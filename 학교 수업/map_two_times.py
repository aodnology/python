# map
# map(f, iterable)은 함수(f)와 반복 가능한(iterable) 자료형을 입력으로 받음
# map은 입력 받은 자료형의 각 요소가 함수 f에 의해 수행된 결과를 묶어서 리턴하는 함수

def two_times(numberList):
    result = []
    for number in numberList:
        result.append(number*2)
    return result

result = two_times([1,2,3,4])
print(result)

def two_times(x):
    return x*2

res = list(map(two_times,[5,6,7,8]))
print(res)

res_2 = list(map(lambda a: a+1, [1,2,3,4]))
print(res_2)