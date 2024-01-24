def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a <b:
        parent[b] = a
    else:
        parent[a] = b

n,m = 7,12
m = [
    [1,2,3],
    [1,3,2],
    [3,2,1],
    [2,5,2],
    [3,4,4],
    [7,3,6],
    [5,1,5],
    [1,6,2],
    [6,4,1],
    [6,5,3],
    [4,5,3],
    [6,7,4]
]
result = 0

m.sort(key=lambda x: x[2])
print(m)
parent = [0] *(n+1)
for i in range(1, n+1):
    parent[i] = i

last = 0 # 최소 신장 트리에 포함되는 간선 중에서 가장 비용이 큰 간선
for a,b,cost in m:
    if find_parent(parent,a) != find_parent(parent, b):
        union_parent(parent, a,b)
        result += cost
        last = cost
  
print(result-last)

