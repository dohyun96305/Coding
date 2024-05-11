# 신나는 함수 실행 
# https://www.acmicpc.net/problem/9184
# 재귀함수 실행에 따른 결과 출력
# 일반 재귀함수 실행시 시간 초과 => 기존 계산한 값에 대해서도 다시 계산하므로 시간 초과
# dp를 통해 계산 결과 저장 및 활용 => Memoization DP
# 20을 넘을경우 초기화되므로 3차원 dp 및 20까지

import sys
input = sys.stdin.readline

def recu_fun(a, b, c, dp) : 
    if a <= 0 or b <= 0 or c <= 0 : 
        return 1
    
    elif a > 20 or b > 20 or c > 20 : 
        return recu_fun(20, 20, 20, dp)
    
    elif dp[a][b][c] : 
        return dp[a][b][c]
    
    elif a < b and b < c : 
        dp[a][b][c] = recu_fun(a, b, c-1, dp) + recu_fun(a, b-1, c-1, dp) - recu_fun(a, b-1, c, dp)
        return dp[a][b][c]
    
    else : 
        dp[a][b][c] = recu_fun(a-1, b, c, dp) + recu_fun(a-1, b-1, c, dp) + recu_fun(a-1, b, c-1, dp) - recu_fun(a-1, b-1, c-1, dp)
        return dp[a][b][c]

dp = [[[0 for _ in range(21)] for _ in range(21)] for _ in range(21)]

while 1:
    a, b, c = map(int, input().split())
    if a==-1 and b==-1 and c==-1:
        break
    
    print(f'w({a}, {b}, {c}) = {recu_fun(a, b, c, dp)}')