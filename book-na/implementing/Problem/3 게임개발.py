
# 왼쪽으로 회전
def turn_left(direction):
    direction -=1
    if direction == -1:
        direction = 3
    return direction

def solution(n,m,info, map):
    d = [[0]*m for _ in range(n)]

    # 현 캐릭터의 x좌표, y좌표, 방향
    x,y,direction = info
    
    d[x][y] = 1

    # 북,동,남,서 방향 정의
    dx = [-1, 0 ,1, 0]
    dy = [0, 1, 0, -1]

    # 시뮬레이션 시작
    count = 1
    turn_time = 0
    while True:
        #왼쪽으로 회전
        direction = turn_left(direction)
        nx = x + dx[direction]
        ny = y + dy[direction]
        #회전한 이후 정면에 가보지 않은 칸이 존재하는 경우
        if d[nx][ny] == 0 and map[nx][ny] == 0:
            d[nx][ny] = 1
            x = nx
            y = ny
            count += 1
            turn_time = 0
            continue
        #회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
        else:
            turn_time += 1
        
        #네 방향 모두 갈 수 없는 경우
        if turn_time == 4:
            nx = x - dx[direction]
            ny = y - dy[direction]
            # 뒤로 갈 수 있다면 이동
            if map[nx][ny] == 0:
                x = nx
                y = ny
            # 뒤가 바다로 막혀있는 경우
            else:
                break
            turn_time = 0

    return count 



print(solution(4,4,[1,1,0], [[1,1,1,1], [1,0,0,1], [1,1,0,1], [1,1,1,1]])) # 3

