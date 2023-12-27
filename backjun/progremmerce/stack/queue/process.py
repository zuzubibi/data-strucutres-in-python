# queue 구현하기 모듈없이
# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/42587

def solution(pri, location):
    queue = [(i,p) for i,p in enumerate(pri)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer +=1
            if cur[0] == location:
                return answer
            



# 연습 2
# def solution(priorities, location):
#     queue = [(i,q) for i,q in enumerate(priorities)]
#     answer = 0

#     while True:
#         cur = queue.pop(0)
#         if any(cur[1] < q[1] for q in queue):
#             queue.append(cur)
#         else:
#             answer += 1
#             if cur[0] == location:
#                 return answer