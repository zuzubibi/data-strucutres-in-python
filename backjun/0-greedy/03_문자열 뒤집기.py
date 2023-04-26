'''
--- 문제 ---
0과 1로만 이루어진 문자열 s를 가지고 있다.
문자열 s에 담긴 모든 수들을 같게 만들려 한다.
s에서 연속된 하나 이상의 숫자를 잡고 모두 뒤집는 것을 할 수 있다.
뒤집는 것이란 1을 0으로, 0을 1로 바꾸는 것을 말한다.

--- test case ---
0001100

정답) 1

--- 문제 접근법 ---
1. 무조건 1번은 다 돌아야 한다.
2. 가장 적은 수를 뒤집는다.

'''

"""
n = '0001100'

result = 0
reverse = False  # 바꾸기
num = int(n[0]) # 첫 번째 수

for i in range(1, len(n)):
    i = int(n[i])
    # 어떤 수가 첫번째 수와 다른 수이고 바꾼 적이 없을 때
    if i != num and reverse == False:
        reverse = True
        # print(i, end=" ")
        # print("here, reversed")
    # 바꾼 적이 있고 어떤 수가 첫번째 수랑 같을 때
    elif reverse == True and i == num:
        result += 1
        reverse = False
        # print(i, end=" ")
        # print("Done, reversed")
    print(i)

print(result)
"""
#------------- 모범 답안 -----------------
# data = input()
data = '0001100'
count0 = 0 # 전부 0으로 바꾸는 경우
count1 = 0 # 전부 1으로 바꾸는 경우

# 첫 번째 원소에 대해서 처리
if data[0] == '1':
    count0 += 1
else:
    count1 += 1

# 두 번째 원소부터 모든 원소를 확인하며
for i in range(len(data)-1):
    if data[i] != data[i+1]:
        #다음 수에서 1로 바뀌는 경우
        if data[i+1] =='1':
            count0 += 1
        #다음 수에서 0으로 바뀌는 경우
        else:
            count1 += 1

print(min(count0, count1))

    
        