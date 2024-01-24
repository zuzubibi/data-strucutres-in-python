# 특정 원소가 속한 집합을 찾기
def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합 합치기
def union_parent(parent, a,b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선(union 연산)의 개수 입력받기
v,e = 7,9
parent = [0] * (v+1) # 부모 테이블 초기화
for i in range(1, v+1):
    parent[i] = i

# 모든 간선을 담을 리스트와 최종 비용을 담을 변수
# cost, a, b
edges = [
    [29,1,2],
    [75,1,5],
    [35,2,3],
    [34,2,6],
    [7,3,4],
    [23,4,6],
    [13,4,7],
    [53,5,6],
    [25,6,7]
]
result = 0


# 간선을 비용순으로 정렬
edges.sort()

# 간선을 하나씩 확인하며
for edge in edges:
    cost, a, b = edge
    # print(cost,a,b)
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        result += cost
        union_parent(parent,a,b)

print(result)
