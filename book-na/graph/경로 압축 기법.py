def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]
#----------------- 아래 코드는 같음 -------------------

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a,b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선(union 연산)의 개수 입력 받기
v,e = 6,4
parent = [0] * (v+1)
e = [
    [1,4],
    [2,3],
    [2,4],
    [5,6]
]

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v+1):
    parent[i] = i

# union 연산을 각각 수행
for a,b in e:
    union_parent(parent, a,b)

# 각 원소가 속한 집합 출력
print("각 원소가 속한 집합: ", end="")
for i in range(1, v+1):
    print(find_parent(parent, i), end=" ")

print()

# 부모 테이블 내용 출력
print("부모 테이블: ", end="")
for i in range(1, v+1):
    print(parent[i], end=" ")
