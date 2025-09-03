# https://school.programmers.co.kr/learn/courses/30/lessons/42578

from collections import Counter

def solution(clothes):
    arr = Counter(clothes)
    print(clothes, arr)
    return 0

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]])) # 5
# print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]])) # 3