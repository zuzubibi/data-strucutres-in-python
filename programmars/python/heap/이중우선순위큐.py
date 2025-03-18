# https://school.programmers.co.kr/learn/courses/30/lessons/42628

'''명령어	수신 탑(높이)
I 숫자   큐에 주어진 숫자를 삽입합니다.
D 1  	큐에서 최댓값을 삭제합니다.
D -1	큐에서 최솟값을 삭제합니다.
'''
# 모든 연산을 처리한 후 큐가 비어있으면 [0,0] 비어있지 않으면 [최댓값, 최솟값]을 return 

from heapq import *
def solution(operations):
    min_heap = []
    max_heap = []

    for el in operations:
        if el[0] == 'I':
            heappush(min_heap, int(el[2:]))
            heappush(max_heap, -1 * int(el[2:]))
        else:
            if len(min_heap) == 0:
                continue
            elif el[2] == '-':
                num = heappop(min_heap)
                max_heap.remove(-1 * num)
            else:
                num = heappop(max_heap)
                min_heap.remove(-1 * num)
    if len(min_heap) == 0:
        return [0,0]
    else:
        return [-1 * heappop(max_heap), heappop(min_heap)]


print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"])) # [0,0]
print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"])) # [333, -45]