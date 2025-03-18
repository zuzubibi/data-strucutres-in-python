from heapq import heapify, heappush, heappop
from collections import Counter # 몇번 만들어지는지 알 수 있음

# x와 가장 가까운 요소로 정렬하기 => (거리: x - el)가 작을 수록 
class Solution:
    def findClosetElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = [(abs(x - el), el) for el in arr]
        heapify(heap)

        answer = []
        for _ in range(k):
            _, el  = heappop()
            answer.append(el)
        return answer
    

# 가장 빈도수가 높은 단어부터 정렬하기 -> 빈도수는 Counter사용, heapq는 minheap이므로 -꼭 붙이기
class Solution2:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word2count = Counter(words)

        heap = []
        for word, count in word2count.items():
            heap.append((-count, word))
        
        heapify(heap)
        answer = []
        for _ in range(k):
            _, word = heappop(heap)
            answer.append(word)
        
        return answer
        
# nums와 k가 주어졌을때 k개의 가장 자주 나오는 element를 return 
class Solution3:
    def topKFrequent2(self, nums: List[int], k: int) -> List[int]:
        num2count = Counter(nums)
        heap = []

        for num, count in num2count.items():
            heap.push((-count, num))
        
        heapify(heap)
        answer = []
        for _ in range(k):
            _, num = heappop(heap)
            answer.append(num)
        return answer