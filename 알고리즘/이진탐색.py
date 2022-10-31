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

a = binary_search(15, [1,3,5,7,9,15,18])
b = binary_search(8, [1,2,3,4,5,6,7,8])
print(a,b)