n, m = 4, 6
array = [19,15,10,17]

start = 0
end = max(array)

# 이진 탐색 수행(반복)
result = 0
while start <= end:
    mid = (start + end) //2
    total = 0

    for x in array:
        # 잘랐을 때 떡의 양
        if x > mid:
            total += x-mid

    # 떡 양이 부족했을 경우 (왼쪽 부분 탐색)
    if total < m:
        end = mid - 1
    # 떡 양이 충분한 경우 덜 자르기 (오른쪽 부분 탐색)
    else:
        result = mid # 최대한 덜 잘랐을 때가 정답이므로, 여기에서 result 기록
        start = mid + 1

print(result)

