# https://school.programmers.co.kr/learn/courses/30/lessons/138477


# 명예의 전당 목록의 점수의 개수 k
# 1일부터 마지막 날까지 출연한 가수들의 점수인 score
# 매일 발표된 명예의 전당의 최하위 점수를 return

from heapq import heappop, heappush, heapify

def solution(k, score):
    heap = []
    answer = []
    for el in score:
        if (len(heap) < k):
            heappush(heap, el)
        elif heap[0] < el:
            heappop(heap)
            heappush(heap, el)
        answer.append(heap[0])
        
    print(score)


    return



solution(3, [10, 100, 20, 150, 1, 100, 200]) # [10, 10, 10, 20, 20, 100, 100]
solution(4, [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]) # [0, 0, 0, 0, 20, 40, 70, 70, 150, 300]