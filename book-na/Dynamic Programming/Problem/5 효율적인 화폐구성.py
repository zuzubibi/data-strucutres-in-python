def solution(arr, m):
    d = [10001]*(m+1)
    
    d[0] = 0
    for i in range(len(arr)):
        for j in range(arr[i], m+1):
            if d[j - arr[i]] != 10001: # (i-k)원을 만드는 방법이 존재하는 경우
                d[j] = min(d[j], d[j- arr[i]] +1)
                
    if d[m] == 10001:
        return -1
    else:
        return d[m]


print(solution([2,3], 15)) #5
print(solution([3,5,7], 4)) #-1