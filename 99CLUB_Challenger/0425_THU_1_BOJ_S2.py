# 최소 힙
# https://www.acmicpc.net/problem/1927

# 자연수 입력시 배열에 자연수 추가 
# 0 입력시 가장 작은 자연수 출력 및 제거, 빈 배열일 때는 0 출력

import heapq
import sys

n = int(input())
temp = []

for i in range(n) : 
    num1 = int(sys.stdin.readline().rstrip())
    
    if num1 == 0 :
        if temp : 
            print(str(heapq.heappop(temp)))
        else : 
            print('0')
    else : 
        heapq.heappush(temp, num1)


