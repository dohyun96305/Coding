# 회전하는 큐
# https://www.acmicpc.net/problem/1021
# 원하는 번호를 popleft() 하기 위해 좌측 혹은 우측으로 회전해야하는 최솟값

from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split()) # 전체 숫자 크기 n개, 뽑고자 하는 숫자 m개 

idxs = list(map(int, input().split())) # popleft() 하고자 하는 번호
n_list = deque([i for i in range(1, n+1)]) # 돌리기 위한 번호 리스트

count = 0

for idx in idxs:
    while True:
        if n_list[0] == idx: # 일치할 경우 popleft() 
            n_list.popleft()
            break

        else:
            if n_list.index(idx) < len(n_list)/2: # 왼쪽으로 돌려야할 경우
                while n_list[0] != idx:
                    n_list.append(n_list.popleft())
                    count += 1

            else:                                 # 오른쪽으로 돌려야할 경우
                while n_list[0] != idx:
                    n_list.appendleft(n_list.pop())
                    count += 1

print(count)