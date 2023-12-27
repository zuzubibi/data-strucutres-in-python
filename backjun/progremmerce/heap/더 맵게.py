from heapq import *

def solution(scoville, K):
    heapify(scoville)
    answer = 0

    while scoville[0] < K:
        mix = heappop(scoville) + heappop(scoville)*2
        heappush(scoville, mix)
        answer += 1

        if len(scoville)==1 and scoville<K:
            return -1

    return answer
    