def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a <b:
        parent[b] = a
    else:
        parent[a] = b

n,m = 7,8
m = [
    [0,1,3],
    [1,1,7],
    [0,7,6],
    [1,7,1],
    [0,3,7],
    [0,4,2],
    [0,1,1],
    [1,1,1]
]
parent = [0]*(n+1)
for i in range(1, n+1):
    parent[i] = i

for x,a,b in m:
    if x == 1:
        if find_parent(parent,a) == find_parent(parent, b):
            print("YES")
        else:
            print("NO")
    else:
        union_parent(parent,a,b)


