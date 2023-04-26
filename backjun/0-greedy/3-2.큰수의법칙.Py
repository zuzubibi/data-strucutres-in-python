"""
--- 문제 ---
다양한 수로 이루어진 배열(arr)이 있다. 
주어진 수를 M번 더해 가장 큰 수를 만들어야 한다.
(단, 배결의 특정한 인덱스(번호)에 해당하는 수가 연속해서 K번 초과해 더해질 수 없다.)

n: arr의 길이

--- test case ---
1.
arr = [2,4,5,4,6]
M = 8
K = 3   일 때,
6 + 6 + 6 + 5 + 6 + 6 + 6 + 5 = 46

2. 
arr = [3,4,3,4,3]
M = 7
K = 2   일 때,
4 + 4 + 4 + 4 + 4 + 4 + 4 = 28

--- 문제 접근법 ---
배열을 정렬해서 가장 큰 수가 k번 반복하도록 만든다.
두번째로 가장 큰 수가 그 다음으로 1번 반복하도록 만든다.
다시 가장 큰 수가 k번 반복하도록 만든다.

m은 무조건 횟수가 차면 끝남
k는 계속해서 반복된다.

"""

# n,m,k = 5,8,3
# arr = [2,4,5,4,6]
n,m,k = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort() # 6,5,4,4,2
first = arr[n-1] # 가장 큰 수
second = arr[n-2] # 두 번째로 큰 수

result = 0

while True:
    # k번 동안 반복
    for i in range(k):
        # 만약 고정횟수 m번을 초과하면 종료
        if m == 0:
            break
        result += first
        m -= 1
    # k번 이상 되어서 나왔고 고정횟수 m번 초과하면 종료
    if m == 0:
        break
    # 2번째 변수 더함
    result += second
    m -= 1

print(result)