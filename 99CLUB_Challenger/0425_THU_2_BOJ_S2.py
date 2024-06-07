# 유기농 배추 
# https://www.acmicpc.net/problem/1012
# 인접한 배추 영역의 개수 return 
# BFS 알고리즘, 연결되어 있는 영역의 개수 Return 

from collections import deque

t = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
  
def bfs(x, y) :
    
    queue = deque()
    queue.append((x, y))
    
    while queue : 
        x, y = queue.popleft()
        
        for i in range(4) : 
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= m or ny < 0 or ny >= n : 
                continue
            
            if graph[nx][ny] == 1 : 
                graph[nx][ny] = 0 
                queue.append((nx, ny))

for a1 in range(t) : 
    count = 0
    n, m, k = map(int, input().split())

    graph = [[0] * n for _ in range(m)]

    for c in range(k) : 
        a, b = map(int, input().split())
        graph[b][a] = 1
        
    for d in range(m) : 
        for e in range(n) : 
            if graph[d][e] == 1 :
                count += 1
                bfs(d, e)
                
    print(count)