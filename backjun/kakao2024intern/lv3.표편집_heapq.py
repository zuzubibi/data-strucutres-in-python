# 이해하기 어려움
# 자료구조 + 구현

from heapq import heapify, heappush, heappop

def solution(n,k,commands):
    max_heap = [-i for i in range(k)]
    min_heap = [i for i in range(k,n)]
    result = ['O' for _ in range(n)]
    undos = []
    heapify(max_heap)
    heapify(min_heap)

    
    for command in commands:
        if command[0] == 'D':
            for _ in range(int(command[2:])):
                heappush(max_heap, -heappop(min_heap))
        elif command[0] == 'U':
            for _ in range(int(command[2:])):
                heappush(min_heap, -heappop(max_heap))
        elif command[0] == 'C':
            num = heappop(min_heap)
            undos.append(num)
            result[num] = 'X'
            if len(min_heap) == 0:
                heappush(min_heap, -heappop(max_heap))
            
        else:
            undo = undos.pop()
            result[undo] = 'O'
            if min_heap[0] > undo:
                heappush(max_heap, -undo)
            else:
                heappush(min_heap, undo)
    return ''.join(result)




print(solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))