# O(log n) : 로그(대수)시간
# 대표적인 예 : 이진검색 알고리즘

# 이진 검색 알고리즘의 특징 
# : 각 프로세스의 스텝을 절반으로 나눠서 진행 n/2 ==> (n/2)/2 를 반복
# 이 과정을 시간복잡도로 표현하면 O(log n) 이 된다.

# 사전 지식
# 로그는 지수의 정 반대이다

# 지수 (곱)
# 2^n = 32 일때 n의 값은?
# 2*2*2*2*2 = 32
# n = 5

# 로그 (나누기)
# n = log2 32 일떼 n의 값은?

# 해답
# : n log2 32 는 
# 32를 2로 몇번을 나누어야 1이 되냐 물어보는 문제이다
# 32 / 2 = 16  // 1
# 16 / 2 = 8   // 2
#  8 / 2 = 4   // 3
#  4 / 2 = 2   // 4
#  2 / 2 = 1   // 5

# 위의 식을 보면 이진 검색 (정렬후 전체 개수에서 반씩 나누는 과정을 반복)과 동일한 문제 접근 방식을 가지고 있음
# 따라서 이진검색의 시간복잡도는 O(log n) 인것이다.

# 이진 탐색(Binary Serarch) 알고리즘
# 이진 탐색 알고리즘은 정렬된 배열에만 사용 가능하다.
# 따라서 정렬된 리스트가 아니면 이 알고리즘은 사용 불가능하다.
# 이진 탐색은 비교를 1번씩 거칠 때마다 탐색 범위가 절반으로 줄어든다 : O(log n)

def binary_search(target, data): # target : 찾고자하는 값, data : 오름차순으로 정렬된 list
    data.sort()                  # 오름차순 정렬
    start = 0                    # data의 처음 값 인덱스
    end = len(data) -1           # data의 마지막 값 인덱스

    while start <= end:         
        mid = (start + end) // 2 # mid : start 와 end 의 중간 인덱스
                                 # 처음 인덱스보다 마지막 인덱스가 크면 반으로 나눔 / O(log n)

        if data[mid] == target:
            return mid           # 함수를 끝냄
        elif data[mid] < target:
            start = mid + 1
        else :
            end = mid - 1

    return None

a = binary_search(1, [1,2,3,4,5,6,7,8])
b = binary_search(8, [1,2,3,4,5,6,7,8])
print(a,b)