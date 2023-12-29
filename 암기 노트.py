def binary_search(array, target, start ,end):
    if start > end:
        return None
    
    mid = (start+end)//2

    # 중간점의 값이 원하는 값과 동일하다면 반환하기
    if array[mid] == target:
        return mid
    # 중간점의 값보다 원하는 값이 작다면 왼쪽 탐색
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    # 중간점의 값보다 원하는 값이 크다면 오른쪽 탐색
    else:
        return binary_search(array, target, mid+1, end)




n, target = 10, 7
array = [1,3,5,7,9,11,13,15,17,19] 

# 이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n-1)
if result == None:
    print('원소가 존재하지 않습니다.')
else:
    print(result+1)
