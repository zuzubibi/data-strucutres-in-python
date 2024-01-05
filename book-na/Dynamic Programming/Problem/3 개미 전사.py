# 문제 
# 일직선에 놓인 식량창고에서 약탈을 하려한다.
# 서로 인접한 곳을 약탈하면 안된다.
# 약탈을 최대로 할 수 있다면 얼마나 약탈할 수 있는지 구해라
# ------------------------------------------------------------------
def solution(n, arr):
    #dp table
    d = [0] * 100

    # dynamic programming
    d[0] = arr[0]
    d[1] = max(arr[0], arr[1]) # 가장 큰 걸로 갱신

    for i in range(2, n): # 두가지 경우의 수 중 가장 큰걸로 갱신
        d[i] = max(d[i-1], d[i-2] + arr[i])

    return d[n-1]


print(solution(4, [1,3,1,5]))