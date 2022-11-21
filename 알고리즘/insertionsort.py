# InsertionSort (삽입정렬) / T(n) = O(n^2)
'''
타겟인 데이터의 앞 데이터들의 크기를 따져서
본인보다 큰 데이터 앞, 작은데이터 뒤에 데이터를 삽입하는 방법
모든 요소를 앞에서부터 아례대로 이미 정렬된 배열부분과 비교하여
자신의 위치를 찾아 삽입한다.
'''

def InsertionSort(arr):
    n = len(arr)
    for i in range(1, n):
        for j in range(i, 0, -1):
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
            else:
                break

arr = [2,7,3,5,4,9]
InsertionSort(arr)
for i in range(len(arr)):
    print("[%d" %arr[i], end="]")
