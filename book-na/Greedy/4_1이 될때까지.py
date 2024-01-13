def solution(n,k):
    result = 0
    while n > 1:
        if n % k == 0:
            n //= k
        else:
            n -= 1
        print(n, result)
        result += 1
    
    return result

# --------------------------------------------------------
def anotherSolution(n,k):
    result = 0

    while True:
        # N==K로 나누어떨어지는 수가 될때까지 1씩 빼기
        target = (n//k)*k
        result += (n-target)
        n = target

        # N이 K보다 작을 떄 (더 이상 나눌 수 없을 때) 반복문 탈출
        if n < k:
            break
        # K로 나누기
        result += 1
        n //= k


    # 마지막 남은 수에 대해 1씩 빼기
    result += (n -1)
    return result


print(solution(25, 5)) # 2
print(solution(25, 3)) # 6