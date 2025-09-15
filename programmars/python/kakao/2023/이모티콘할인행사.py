#https://school.programmers.co.kr/learn/courses/30/lessons/150368

# 풀이 1
from itertools import product

def solution(users, emoticons):
    discount_rates = [10, 20, 30, 40]
    result = []

    # 이모티콘 별 할인율의 모든 조합(중복 순열) 구하기
    discount_cases = list(product(discount_rates, repeat=(len(emoticons))))
    
    for discount_case in discount_cases:
        member = 0
        income = 0
        for required_discount, budget in users:
            purchased = 0

            for i in range(len(emoticons)):
                # 각 사용자가 구매할 이모티콘
                # 각 조합별 모든 이모티콘을 순회하며 경우의 수 구하기
                if required_discount <= discount_case[i]:
                    # 한 사용자 구매액은 자신의 기준 할인율 이상 할인하는 이모티콘의 할인가
                    purchased += int(emoticons[i] - emoticons[i]*discount_case[i] *0.01)
            if purchased >= budget:
                member += 1
            else:
                income += purchased
        # 할인율 조합별 (총 가입자 수, 판매액)을 배열에 저장
        result.append((member, income))
    # 조합별 가장 가입자 수 > 판매액 순으로 큰 경우를 찾아 리턴
    result.sort(reverse=True, key= lambda x: (x[0], x[1]))
    # print(result[0])
    return list(result[0])

# 풀이 2
def solution2(users, emoticons):
    answer_user = answer_price = 0
    for comb in yield_discount_rate_price_combination(emoticons, []):
        comb_user = comb_price = 0
        for criteria_rate, criteria_price in users:
            price = sum(map(lambda x: x[1], filter(lambda x: x[0] >= criteria_rate, comb)))
            if price >= criteria_price:
                comb_user += 1
            else:
                comb_price += price
        if comb_user > answer_user or (comb_user == answer_user and comb_price > answer_price):
            answer_user, answer_price = comb_user, comb_price
    return [answer_user, answer_price]

def yield_discount_rate_price_combination(emoticons, prefix):
    if not emoticons:
        yield prefix
        return
    for i in range(10, 50, 10):
        price = emoticons[0] * (1 - i * 0.01 )
        yield from yield_discount_rate_price_combination(emoticons[1:], prefix + [(i, price)])


print(solution2([[40, 10000], [25, 10000]], [7000, 9000])) #[1, 5400]
print(solution2([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]], [1300, 1500, 1600, 4900])) #[4, 13860]