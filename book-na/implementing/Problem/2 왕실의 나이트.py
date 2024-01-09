def solution(s):
    li ={v:i+1 for i, v in enumerate(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])}
    x, y = li[s[0]], int(s[1])

    dx = [1,-1,2,2,1,-1,-2,-2]
    dy = [2,2,-1,1,-2,-2,1,-1]
    cnt = 0

    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx < 1 or ny < 1 or nx > 8 or ny > 8:
            continue

        cnt += 1
    
    return cnt 
#----------------------------------------------------------------------------------
def teacherSolution(s):
    row= int(s[1])
    column = int(ord(s[0])) - int(ord('a')) + 1

    # 나이트가 이동할 수 있는 8가지 방향 정의
    steps = [(-2,-1), (-1,-2), (1,-2), (2,-1), (2,1), (1,2), (-1,2), (-2, 1)]

    # 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
    result = 0
    for step in steps:
        #이동하고자 하는 위치 확인
        next_row = row + step[0]
        next_column = column + step[1]
        
        # 해당 위치로 이동이 가능하면 카운트 증가
        if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <=8:
            result += 1
    return result 

print(solution('a1')) # 2
print(solution('c2')) # 6