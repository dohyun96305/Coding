# 계단 오르기 
# https://acmicpc.net/problem/2579
# DP 문제, 최대 점수 return 
# 계단은 한번에 1개 혹은 2개씩만
# 연속된 3개의 계단 X
# 마지막 도착계단은 밟음

import sys

n = int(input())
score = []
for i in range(n) : 
    score.append(int( sys.stdin.readline().rstrip() ))
    
score1 = [0] + score

if n <= 2 : 
    print(sum(score1))
else :     
    temp = [0] * 301 # 빈 list 생성 
    temp[1] = score1[1]
    temp[2] = score1[1] + score1[2]

    for i in range(3, n+1) : 
        temp[i] = max(temp[i-3] + score1[i-1] + score1[i], temp[i-2] + score1[i])

    print(temp[n])

