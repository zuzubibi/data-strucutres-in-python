'''
방송에서 먹을 음식 n개가 있음. 각 음식을 섭취하는데 일정시간이 걸린다. 1번 음식부터 먹고 번호가 증가하는 순서대로 음식을 먹음
마지막 번호 음식 이후 다시 1번 음식으로 돌아온다. k초 이후 네트워크 장애로 잠시 중단함.
방송을 다시 시작할 때 몇번 음식부터 다시 먹으면 되는지 알아보자
food_times: 음식을 모두 먹는데 걸리는 시간
solution(): 네트워크장애 시간 k초가 매개변수로 주어질 때 몇 번 음식부터 다시 섭취하면 되는지 return
'''
def solution(k):
    return 

# food_times = list(map(int, input().split()))
# k = int(input())
food_times = [3,1,2]
k = 5

last_time = 0
while True:
    for i in range(len(food_times)):
        if k == 0:
            break
        food_times[i] -= 1
        k -= 1
        last_time +=1
    