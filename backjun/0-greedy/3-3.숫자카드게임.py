"""
--- 문제 ---
숫자 카드 게임: 여러 숫자 카드 중에서 가장 높은 숫자 카드 한 장을 뽑는 게임
1. 숫자가 쓰인 카드들이 N * M 형태로 놓여 있다. 이 때 N은 행의 개수, M은 열의 개수
2. 먼저 뽑고자 하는 카드가 포함되어 있는 행을 선택
3. 그 다음 선택된 행의 카드들 중 가장 숫자가 낮은 카드 뽑음
4. 따라서 처음에 카드를 골라낼 행을 선택할 때, 이후에 해당 행에서 가장 숫자가 낮은 카드를 뽑을 것을 고려해
   최종적으로 가장 높은 숫자의 카드를 뽑을 수 있도록 전략을 세워야 함

--- test case ---
1. 

3 3
3 1 2
4 1 4
2 2 2

정답) 2

2.

2 4
7 3 1 8
3 3 3 4

정답) 3
"""

n, m = map(int, input().split())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]
# n,m = 2, 4
# arr = [[7, 3, 1, 8], [3, 3, 3, 4]]

# n,m = 3, 3
# arr = [[3,1,2],[4,1,4],[2,2,2]]

_min = 9999

result = 0

for i in arr:
    if min(i) < _min:
        _min = min(i)
        num = i
    else:
        result = min(i)

print(result)

#-------------------모범 답안--------------------------   
# n,m 을 공백으로 구분하여 입력받기
n,m = map(int,input().split())

result = 0
# 한 줄씩 입력받아 확인
for i in range(n):
    data = list(map(int, input().split()))
    # 현재 줄에서 '가장 작은 수' 찾기
    min_value = min(data)

    #'가장 작은 수'들 중에서 가장 큰 수 찾기
    result = max(min_value, result)
print(result)