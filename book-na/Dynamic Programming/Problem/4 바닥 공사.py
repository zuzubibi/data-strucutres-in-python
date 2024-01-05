def solution(x):
    # dp table
    d = [0] *1001

    # dynamic programming
    d[1] = 1
    d[2] = 3
    for i in range(3, x+1):
        d[i] = (d[i-1] + 2 * d[i-2]) % 796796


    return  d[x]


print(solution(3))