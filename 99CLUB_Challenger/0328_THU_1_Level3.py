# 가장 먼 노드 
# https://school.programmers.co.kr/learn/courses/30/lessons/49189
# BFS 문제 

from collections import deque

def solution(n, edge):
    
    visited = [True] * (n+1)
    visited[1] = False
    
    len1 = [0] * (n+1)
    
    temp = {(x+1) : [] for x in range(n)}
    
    for a,b in edge : 
        temp[a] += [b]
        temp[b] += [a]
        
    queue = deque()
    queue.append(1)
    
    while queue :     
        key = queue.popleft()
        list1 = temp[key]
        
        for a in list1 : 
            if visited[a] : 
                visited[a] = False
                len1[a] = len1[key] + 1
                queue.append(a)
        
    return len1.count(max(len1))