# O(1) : 상수 시간 / 문제를 처리하는데 오직 한 단계(한 스텝)만 처리함
# 시간복잡도가 O(1) 인 경우
# 입력값의 크기와 관계 없이, 즉시 출력값을 얻어 낼 수 있다는 의미
# 즉 스텍값이 1인 경우

arr = ["a","b","c","d","e","f","g"]

def O_1(arr, index):
    return arr[index]

a = O_1(arr, 0)
b = O_1(arr, 1)
print(a)
print(b)