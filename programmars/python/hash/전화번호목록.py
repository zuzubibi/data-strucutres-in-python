# https://school.programmers.co.kr/learn/courses/30/lessons/42577

# 문제 풀이 방법
# 1. loop를 활용 (완전탐색)
# 2. sorting/ loop 활용
# 3. hash 활용

def solution(phone_book):

    # 1. 비교할 A 선택
    for i in range(len(phone_book)):
        # 2. 비교대상 B 선택
        for j in range(i+1, len(phone_book)):
            # 3. 서로 비교
            if (phone_book[j].startswith(phone_book[i])):
                return False
            if (phone_book[i].startswith(phone_book[j])):
                return False
    return True


def solution2(phone_book):
    # 1. 전화번호 sorting
    phone_book.sort()
    
    # 2. sorting한 전화번호를 2개씩 확인해서 접두어인지 확인
    for i in range(len(phone_book) - 1):
        if (phone_book[i+1].startswith(phone_book[i])):
            return False
    return True

def solution3(phone_book):
    # 1. 전화번호 sorting
    phone_book.sort()
    # 2. zip을 사용해서 비교 (zip의 결과값이 딕셔너리임)
    for t1, t2 in zip(phone_book, phone_book[1:]):
        if t2.startswith(t1):
            return False
    return True
    

from collections import Counter
def solution4(phone_book):
    phone_book.sort(key=len, reverse=True)
    # 1. hash Map을 만든다. (검색하려고 만듦)
    arr = Counter(phone_book)

    # 2. 접두어가 Hash map에 존재하는지 찾는다.
    for nums in phone_book:
        jubdo = ''
        for num in nums:
            jubdo += num

            # 3. 접두어를 찾아야 한다. (기존 번호와 같은 경우는 제외)
            if jubdo in arr and jubdo != nums:
                return False
    return True


print(solution4(["119", "97674223", "1195524421"])) # false
print(solution4(["123","456","789"])) # true
print(solution4(["12","123","1235","567","88"])) # false