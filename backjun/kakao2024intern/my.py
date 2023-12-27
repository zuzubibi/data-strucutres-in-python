# 자료구조 + 구현

N = 10**9
class Node:
    survived =True 

    def __init__(self, p, n):
        self.prev = p if p >=0 else None
        self.next = n if n <N else None

def solution(n,k,command):
    global N
    N = n
    table = {i: Node(i-1, i+1) for i in range(n)}
    current = k
    removed = []

    for com in command:
        if com == 'C': # 삭제
            table[current].survived = False
            removed.append(current)

            # 현재 노드 위치의 앞 뒤
            prev, next = table[current].prev, table[current].next
            # prev의 다음을 현재 노드의 다음으로 연결
            if prev is not None: table[prev].next = table[current].next
            # next의 이전을 현재 노드의 이전으로 연결
            if next is not None: table[next].prev = table[current].prev 
            
            # 노드 제거 (current 위치 설정)
            if table[current].next is None: # 다음 노드가 없음
                current = table[current].prev
            else: # 다음 노드가 있음
                current = table[current].next

        elif com == 'Z': # 실행 취소
            recovered = removed.pop()
            table[recovered].survived = True

            # 현재 노드
            prev, next = table[recovered].prev, table[recovered].next
            # 이전 노드 연결
            if prev is not None: table[prev].next = recovered
            # 이후 노드 연결
            if next is not None: table[next].prev = recovered

        else:
            c, amount = com.split()
            if c == 'U':
                for _ in range(int(amount)):
                    current = table[current].prev
            elif c == 'D':
                for _ in range(int(amount)):
                    current = table[current].next

    return ''.join(["O" if table[i].survived else "X" for i in range(n)])


print(solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))