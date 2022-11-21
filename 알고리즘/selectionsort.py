# Selection Sort(선택정렬) / T(n) = O(n^2)
'''
입력 배열 전체에서 최솟값을 선택한 뒤 배열의 0번 원소와 자리를 바꾸고
다음 정렬시에 0번 원소를 제외한 나머지 원소에서 최솟값을 선택해 1번 원소와 자리를 바꾸는
과정을 반복하여 최솟값을 배열 앞번 인덱스에 위치시켜 정렬해나가는 방법이다.

그러므로 정렬된 값을 배열의 맨 앞부터 하나씩 채워나가기 때문에 
뒤에 있는 인덱스로 갈수록 비교 범위가 하나씩 줄어드는 특성을 가지고 있다.
'''

def selection_sort(arr):
    for i in range(len(arr) -1):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

'''
12 : 마지막 연산은 하지 않아도 되기 때문에 배열의 길이 -1 (마지막 인덱스는 확정적으로 가장 큰수가 위치함)
13 : 가장 작은 값을 저장할 변수에 i를 대입
15 : 배열에서 최솟값 찾기
16 : 그 값을 변경
18 : 최솟값이 있는 인덱스번호의 원소를 대입
'''

arr = [8,4,7,2,1]
print(len(arr))
selection_sort(arr)
for i in range(len(arr)):
    print("[%d" %arr[i], end="]")