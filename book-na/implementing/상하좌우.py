# 문제 
# 상하좌우로 갈 수 있는 정사각형 N x N 이 있다.
# L: 왼쪽으로 한 칸 이동
# R: 오른쪽으로 한 칸 이동
# U: 위쪽으로 한 칸 이동
# D: 아래쪽으로 한 칸 이동
# 여행가가 최종적으로 도착할 좌표를 출력하라
#-------------------------------------------------------------------
def solution(n, arr):
    
    here= [1,1]

    for i in arr:
        if i == 'R':
            here[1] += 1
            if here[1] > n:
                here[1] = n

        elif i =='L':
            here[1] -= 1
            if here[1] < 1:
                here[1] = 1

        elif i == 'U':
            here[0] -= 1
            if here[0] < 1:
                here[0] = 1
        elif i == 'D':
            here[0] += 1
            if here[0] > n:
                here[0] = n
    
    print(here)
    return ' '.join([str(i) for i in here])
# --------------------------------------------------------------------------------------
def teacherSolution(n, plans):
    x,y = 1,1

    # L,R,U,D의 이동 방향
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    move_type = ['L', 'R', 'U', 'D']

    # 이동 계획을 하나씩 확인
    for plan in plans:
        # 이동 후 좌표 확인
        for i in range(len(move_type)):
            if plan == move_type[i]:
                nx = x + dx[i]
                ny = y + dy[i]
        
        # 공간을 벗어나는 경우 무시
        if nx < 1 or ny < 1 or nx > x or ny > n:
            continue

        # 이동 수행
        x,y = nx,ny

    # print(x,y)
    return (x,y)
print(teacherSolution(5, ['R', 'R', 'R', 'U', 'D', 'D']))