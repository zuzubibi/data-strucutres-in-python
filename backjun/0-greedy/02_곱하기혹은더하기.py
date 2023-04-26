"""
--- 문제 ---
각 자리가 숫자(0~9)로만 이루어진 문자열S가 주어진다.
왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며,
숫자 사이에 'x'혹은'+'연산자를 넣어 결과적으로 가장 큰 수를 구하는 프로그램을 작성하세요.


---test case---
02984

정답) 576

567

정답) 210

--- 문제 접근법 ---
1. 문자열을 정렬한다.
2. 작은 수 0이나 1이면 연산자 "+"를, 나머지 수면 연산자 "x"를 선택한다.
"""

n = '567'

n = list(n)
n.sort(reverse=True)

result = int(n[0])

for i in n[1:]:
    i = int(i)
    if i in [0, 1]:
        result += i
    else:
        result *= i

print(result)

#------------- 모범 답안 -----------------
data = input()

# 첫 번째 문자를 숫자로 변경하여 대입
result = int(data[0])

for i in range(1, len(data)):
    # 두 수 중에서 하나라도 '0' 혹은 '1'인 경우, 곱하기보다는 더하기 수행
    num = int(data[i])
    if num <=1 or result <=1:
        result += num
    else:
        result *= num
    
print(result)
