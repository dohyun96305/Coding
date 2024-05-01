# 분해합 
# https://www.acmicpc.net/problem/2231
# n이 주어지고 k에 대해 k의 각 자리합과 k의 합이 n을 만족하는 가장 작은 k
# Brutal_Force 문제

n = int(input())
answer = 0

for i in range(1, n+1):
    nums = list(map(int, str(i))) # k에 대해 자리합을 구하기 위해 분해
    answer = sum(nums) + i # k의 분해합
    
    if answer == n:
        print(i)
        break
        
    if i == n: # 끝까지 왔을 때 해당이 없으면 0
        print(0)