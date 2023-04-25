from itertools import combinations

vowels = ('a','e','i','o','u')
l,c = map(int, input().split())

# 가능한 암호를 사전식으로 출력해야 하므로 입력 이후에 정렬 수행
arr = list(input().split())
arr.sort()

# 길이가 l인 모든 암호 조합을 확인
for x in combinations(arr, l):
    # 패스워드에 포함된 각 문자를 확인하여 모음의 갯수 확인
    count = 0
    for i in x:
        if i in vowels:
            count += 1
    
    # 최소 1개의 모음과 최소 2개의 자음이 있는 경우 출력
    if count>=1 and count <= l-2:
        print(''.join(x)) 