def solution(n,m, arr):
    result = set()
    for i in range(n):
        result.add(min(arr[i]))
    
    return max(result)

# ----------------------------------------------------------------------
def anotherSolution(n,m,arr):
    result = 0

    for i in range(n):
        min_value = min(arr[i])
        
        result = max(result, min_value)



print(solution(3,3, [[3,1,2], [4,1,4], [2,2,2]])) # 2
print(solution(2,4, [[7,3,1,8], [3,3,3,4]])) # 3