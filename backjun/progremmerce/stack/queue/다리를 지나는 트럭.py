# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/42583

def solution(bridge_length, weight, truck_weights):
    bridge = [0] * bridge_length # 지나려는 다리 길이
    answer = 0 # 최종 시간
    temp = 0

    while bridge:
        answer +=1
        temp -= bridge.pop(0)

        if truck_weights:
            if temp + truck_weights[0] <= weight: # 차 무게 추가
                t = truck_weights[0]
                temp = truck_weights.pop(0)
                bridge.append(t)
            
            else: # 공기 추가
                bridge.append(0)
        
    return answer