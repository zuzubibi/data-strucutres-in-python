# 개어려움
# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/42584


# 풀이 1
def solution(prices):
    answer = [0]*len(prices)
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]: # 크지 않으면 올려줌
                answer[i] += 1
            else: # 근데 크면 올리고 멈춤
                answer[i] += 1
                break 

    return answer


# 풀이 2
from collections import deque
def solution(prices):
    prices = deque(prices)
    answer = []

    while True:
        cur = prices.popleft()  # issue1) popleft 메서드 외우기
        count = 0
        for i in prices:
            if cur > i:
                count += 1
                break # 첫번째 있는게 다른 price보다 놓다면 그만해야지
            count +=1
        answer.append(count)

    return answer
