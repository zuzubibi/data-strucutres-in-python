"""
--- 문제 ---
어떤 수 N이 1일 될 때까지 아래의 과정을 반복적으로 선택하여 수행하려한다.
1. N-1
2. N/K (단, N이 K로 나누어 떨어질 때)

N과 K가 주어질 때, N이 1이 될 때까지 1번 혹은 2번의 과정을 수행해야 하는 최소 횟수를 구하는 프로그램을 작성하시오.

--- test code ---
N = 17
K = 4  일때,
1번과정 이후, N - 1 = 16
2번과정 이후, N / K = 16 / 4 = 4
2번과정 이후, N / K = 4 / 4 = 1

=> 전체 과정을 실행한 횟수 = 3회
"""

n,k = map(int, input().split())

count = 0

while True:
    if n == 1:
        break
    # 2번 조건
    if n % k == 0:
        n /= k
        count += 1
    # 1번 조건
    else:
        n -= 1
        count += 1
print(count)

#--------- 모범답안 -----------
'''
n,k = map(int, input().split())
result = 0

#n이 k 이상이라면 k로 계속 나누기
while n >= k:
    # n이 k로 나누어 떨어지지 않는다면 n에서 1씩 빼기
    while n % k != 0:
        n -= 1
        result += 1
    # k로 나누기
    n //= k
    result += 1

# 마지막으로 남은 수에 대하여 1씩 빼기
while n > 1:
    n -= 1
    result += 1

print(result)
'''