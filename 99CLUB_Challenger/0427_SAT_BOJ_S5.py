# 요세푸스 문제 0
# https://www.acmicpc.net/problem/11866
# n, m에 대해서 n명의 사람에 대해 k번쨰 사람을 계속 제거할 떄 나오는 순서

import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int, input().split())

array = [i+1 for i in range(n)]
array = deque(array)

temp = []
answer = []
count = 0

while len(answer) < n : 
    
    while array :  
        temp.append(array.popleft())
        count += 1
        
        if count == m : 
            answer.append(temp.pop())
            count = 0
            
    array = deque(temp)
    temp = []

print('<', end = '')
for i in range(n) : 
    if i != n-1 : 
        print(answer[i], end = ', ')
    else : 
        print(answer[i], end = '')
print('>')