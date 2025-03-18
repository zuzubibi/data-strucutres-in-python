# 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)

# 모든 음식의 스코빌 지수가 K 이상이 될 때까지 반복
# Leo가 가진 음식의 스코빌 지수를 담은 배열 scoville
# 원하는 스코빌 지수 K
# 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 섞어야 하는 최소 횟수 return

from heapq import *
def solution(scoville, K):
    heapify(scoville)
    answer = 0

    while scoville[0] < K:
        mix = heappop(scoville) + (heappop(scoville) * 2)
        heappush(scoville, mix)
        answer += 1

        if len(scoville) == 1 and scoville[0] < K:
            return -1
    return answer


# test case 1
arr = [1, 2, 3, 9, 10, 12]
k = 7

print(solution(arr, k)) # 2


# 문제의 핵심
# 1. 힙은 최소/ 최대 일때 사용한다.
# 2. 힙의 첫 요소만 최소/최대이다.
