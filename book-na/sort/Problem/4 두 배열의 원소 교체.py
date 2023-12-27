n,k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()
print(a)
print(b)

a[:k] = b[-k:]
print(a)
print(sum(a))
