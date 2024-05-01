# 다리 짓기 
# https://www.acmicpc.net/problem/1010

# 서쪽 : n개, 동쪽 : m개
# n <= m

# 서쪽 n개만큼, 서로 교차 X
# 조건 하 다리를 놓을 수 있는 경우의 수 

import sys

n1 = int(input())

for i in range(n1) : 
    a, b = map(int, sys.stdin.readline().rstrip().split())
    
    dp = [[0]*(b+1) for _ in range(a+1)]
    
    for j in range(1, b+1) : 
        dp[1][j] = j
        
    for m in range(2, a+1) : 
        for n in range(m, b+1) : 
            dp[m][n] = dp[m][n-1] + dp[m-1][n-1]
            
    print(dp[a][b])