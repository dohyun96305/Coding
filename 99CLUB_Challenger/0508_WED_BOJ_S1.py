# 정수 삼각형
# https://www.acmicpc.net/problem/1932
# dynamic programming, 위 왼쪽 혹은 위 오른쪽 더해서 최댓값 구하기 

n = int(input())
dp = []

for i in range(n) :                                  # dp 생성 
    dp.append(list(map(int,input().split())))

for j in range(1, n) :
    for k in range(j+1) : 
        if k == 0 :                                  # 처음일 경우 
            dp[j][k] += dp[j-1][k]
        elif k == j :                                # 끝일 경우 
            dp[j][k] += dp[j-1][k-1]
        else : 
            dp[j][k] = max(dp[j-1][k-1], dp[j-1][k]) # 그 외 경우 
            
print(max(dp[n-1]))