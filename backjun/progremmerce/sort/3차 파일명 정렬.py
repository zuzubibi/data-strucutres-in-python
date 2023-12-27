# 풀이한 날: 23-12-27
# 난이도: 개쌉 어려움 하지만 생각하면 풀 수 있음
# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/17686
# ---------------------------------------------------------------------
# 전략
# 각 요소는 HEAD, NUMBER, TAIL로 나뉜다. 
# HEAD는 대소문자를 구분하지 않는다.
# NUMBER에서 01과 1은 같은 것으로 본다. 
# NUMBER에 담기는 수는 최대 5자리이다.
# "img34je3.jpg" 라는 예시에서 HEAD = 'img', NUMBER = '34', TAIL='je3.jpg' 이어야 한다.
# 같은 수로 나왔을 땐, 가장 먼저 앞에 온 요소가 가장 먼저 와야 한다.
def solution(files):
    answer = []
    # 1. 각 요소를 head, number, tail로 나누기
    for indx, file in enumerate(files):
        head, number, tail = '', '', ''

        number_check = False # 숫자일 때 감지
        str_check = False # 숫자였다가 다시 문자로 바뀔때 감지

        for i in range(len(file)):
            if str_check==False and len(number) < 5 and file[i].isdigit(): # Number
                number += file[i]
                number_check = True
            elif number_check == False: # Head
                head += file[i]
            else: # Tail
                tail += file[i]
                str_check = True
        print(head, number, tail)    
        answer.append((file, head, number, indx))
    
    # 2. (1)haed를 대소문자를 구분하지 않는 상태에서 정렬 -> (2) number에서 숫자로 변환 후 정렬
    answer.sort(key= lambda x: (x[1].lower(), int(x[2]), x[3]))
    
    return [ ''.join(t[0]) for t in answer]



# test case
arr = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
print(solution(arr)) # 답: ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"]

arr2 = ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]
print(solution(arr2)) # 답: ["A-10 Thunderbolt II", "B-50 Superfortress", "F-5 Freedom Fighter", "F-14 Tomcat"]

arr3 = ["O00321", "O49qcGPHuRLR5FEfoO00321"]
print(solution(arr3)) # ["O49qcGPHuRLR5FEfoO00321", "O00321"]