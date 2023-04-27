'''
설탕을 정확히 n킬로그램 배달해야함
설탕공장에서 만드는 설탕은 봉지에 나눠져 있음 봉지는 3,5킬로그램 봉지임

최대한 적은 봉지를 들고 가려함 예를 들어, 18킬로그램 배달있으면 3킬로그램 6개도 좋지만,
5킬로그램 3개랑 3킬로그램 1개 배달하면 더 적음

설탕을 정확히 n킬로그램 배달시, 봉지 몇 개를 가져가면 되는지 수를 구하는 프로그램 작성하기~
'''

n = 4
arr = [3,5]
arr.sort(reverse=True)
count =0

for i in arr:
    if n % i ==0:
        count += n//i
        
    count += n//i
    n %= i
    if count ==1:
        count = -1
    print(n, i)


print(count)