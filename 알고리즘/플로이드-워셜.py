"""
목표 : 모든 정점 사이의 최단 경로 찾기
시간 복잡도 o(n^3) = (n-1) x O(n^2) / 삼중 for문
"""

"""
과정 :
1. 하나의 정점에서 다른 정점으로 바로 갈 수 있으면 최소 비용을, 
   갈 수 없다면 INF로 배열에 값을 저장
2. 3중 for문을 통해 거쳐가는 정점을 설정한 후 해당 정점을 거져가서
  비용이 줄어드는 경우에는 값을 바꿈
3. 위의 과정을 반복해 모든 정점 사이의 최단 경로를 탐색
"""

import sys

INF = sys.maxsize # 양의 무한대 (가장 큰 값으로 지정) 음의 무한대 : -inf
# INF = int(1e9)  # 말도 안돼는 큰수를 대입해서 최대값 지정

# 노드의 개수 및 간선의 개수를 입력받기
n = int(input('노드 개수 입력 :'))
m = int(input('간선 개수 입력 :'))
# 2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화

graph = [[INF] * (n + 1) for _ in range(n + 1)]
# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력 받아, 그 값으로 초기화
for _ in range(m):
    # A에서 B로 가는 비용은 C라고 설정
    a, b, c = map(int, input().split())
    graph[a][b] = c
'''
점화식에 따라 플로이드 워셜 알고리즘을 수행

점화식 (Recurrence Relation)
: 수열의 일반항을 한 개 이상의 앞선 항들을 이용하여 나타낸 식이다. 
  즉, 어떤 함수를 표현할 때 자신보다 더 작은 변수에 대한 함수와의 관계나 
  자신과 똑같은 함수를 이용해 나타내는 것으로, 
  이는 자기 호출을 사용하는 함수(재귀)의 복잡도를 구하는데 유용하게 사용된다.
'''
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행된 결과를 출력
for a in range(1, n + 1):
    for b in range(1, n + 1):
        # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
        if graph[a][b] == 1e9:
            print("INFINITY", end=" ")
        # 도달할 수 있는 경우 거리를 출력
        else:
            print(graph[a][b], end=" ")
    print()