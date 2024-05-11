# 분해합 
# https://www.acmicpc.net/problem/2231
# 분해합 : N과 N을 이루는 각 자리수의 합 
# 주어진 N에 대해 N을 분해합으로 가지는 가장 작은 수 

n = int(input())
answer = 0

for i in range(1, n+1):
    nums = list(map(int, str(i)))
    answer = sum(nums) + i
    
    if answer == n:
        print(i)
        break
        
    if i == n:
        print(0)