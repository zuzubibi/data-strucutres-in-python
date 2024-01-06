def solution(n,m,k,arr):
    arr.sort(reverse=True)
    cnt = k
    result = 0
    for i in range(m):
        if cnt == 0:
            result += arr[1]
            cnt = k
        else:
            result += arr[0]
            cnt -= 1
    return result 

# =============================================================================
def anotherSolution(n,m,k,arr):
    arr.sort()
    first = arr[n-1] 
    second = arr[n-2]

    # 가장 큰 수가 더해지는 횟수 계산
    count = int(m / (k+1)) * k
    count += m%(k+1)

    result = 0
    result += count * first # 가장 큰 수 더하기
    result += (m - count) * second # 두 번째로 큰 수 더하기

    return result




print(solution(5,8,3,[2,4,5,4,6])) # 46
