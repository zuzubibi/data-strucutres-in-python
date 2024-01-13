# floyd warshall 문제
def solution(n,m,arr,x,k):
    INF = int(1e9)

    graph = [[INF]*(n+1) for _ in range(n+1)]

    # 자기 자신에서 자기 자신으로 가는 비용을 0으로 초기화
    for a in range(1, n+1):
        for b in range(1, n+1):
            if a == b:
                graph[a][b] = 0
    
    # 각 간선에 대한 정보를 입력받아 그 값으로 초기화
    for i in range(m):
        # A와 B가 서로에게 가는 비용은 1이라 설정
        a,b = arr[i]
        graph[a][b] = 1
        graph[b][a] = 1

    # 점화식에 따라 플로이드 워샬 알고리즘 수행
    for k in range(1, n+1):
        for a in range(1, n+1):
            for b in range(1, n+1):
                graph[a][b] = min(graph[a][b], graph[a][k] +graph[k][b])
    
    # 거쳐 갈 노드 K와 최종 목적지 노드 X
    # 수행된 결과를 출력
    distance = graph[1][k] + graph[k][x]

    # 도달할 수 없는 경우, -1 출력
    if distance >= INF:
        return -1
    # 도달할 수 있다면, 최단 거리 출력
    else:
        return distance
                

arr = [
    [1,2],
    [1,3],
    [1,4],
    [2,4],
    [3,4],
    [3,5],
    [4,5]
]
print(solution(5,7, arr,4,5))