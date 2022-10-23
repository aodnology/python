# O(N) : N : N
# input값이 N일때 N개의 스텝(연산횟수)이 필요한 경우

# O(Big-oh)-표기: 점근적 상한
# 알고리즘의 시간복잡도를 표현할때 사용한다.
# 알고리즘의 시간복잡도는 초단위의 속도를 표현 하는 것이 아니고 입력에 대한 스텝(완료까지 걸리는 절차의 수)를 가지고 표현한 것이다
# 단적인 예로 같은 결과를 내는 알고리즘인데 결과를 도출하기위해 적용되는 스텝이 10번인 알고리즘보다 스텝이 5번인 알고리즘이 더 효율적이라 표현 할 수 있다.

# Linear search 알고리즘(선형검색)의 경우 한개씩 검색을 한다
# 만약 데이터가 10개라면 원하는 결과 값을 찾기까지 10번의 스텝이 필요하다
# 따라서 인풋 사이즈가 N이라면 선형 알고리즘은 N스텝이 필요하다.
# 즉 선형 검색 알고리즘의 시간 복잡도는 O(N) 이다.
# 선형검색의 시간 복잡도 = O(N)

# 위와 같이 O(Big-Oh)를 사용하면 시간복잡도를 빠르게 설명할 수 있다.

# 시간복잡도가 O(N) 코드의 예

def linear_search(target, some_list): # target : 찾는 숫자, some_list : 숫자 리스트
    for i in range(len(some_list)):   # for반복문과 len() 함수를 사용해 some_list의 크기 만큼 반복
        if target == some_list[i]:    # target(찾는숫자) == some_list[i] 인경우
            return i                  # 결과 값으로 i를 돌려줌

a = linear_search(1, [7,6,5,4,3,2,1])
b = linear_search(5, [7,6,5,4,3,2,1])

print(a, b)


# while

def linear_search2(target, some_list):
    i = 0
    while i < len(some_list):
        if target == some_list[i]:
            return i
    i += 1
    return None


