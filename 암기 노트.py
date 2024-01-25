# 위상 정렬 알고리즘
from collections import deque

# 노드의 개수와 간선의 개수 입력받기
v, e = 7,8
# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0]*(v+1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트(그래프) 초기화
graph = [[] for _ in range(v+1)]

# 방향 그래프의 모든 간선 정보를 입력받기
e = [
    [1,2],
    [1,5],
    [2,3],
    [2,6],
    [3,4],
    [4,7],
    [5,6],
    [6,4]
]

for a,b in e:
    graph[a].append(b)
    indegree[b] += 1

# 위상 정렬 알고리즘
def topology_sort():
    result = []
    q = deque()

    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)
    
    # 큐가 빌때까지 반복
    while q:
        now = q.popleft()
        result.append(now)
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[now]:
            indegree[i] -= 1
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)
    
    # 위상 정렬을 수행한 결과 출력
    for i in result:
        print(i, end=" ")
topology_sort()

