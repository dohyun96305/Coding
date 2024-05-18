# 바이러스 
# https://www.acmicpc.net/problem/2606
# BFS를 통해 1번과 연결된 node의 수를 구하기

from collections import deque

n = int(input())
m = int(input())

graph = [[]*(n+1) for _ in range(n+1)]

for i in range(m) : 
    a,b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]

visited1 = [False] * (n+1)

def bfs(lis, start, visited) : 
    count = -1
    queue = deque()
    queue.append(start)
    
    while queue : 
        k = queue.popleft()
        count += 1
        visited[k] = True
        
        for i in lis[k] : 
            if not visited[i] :
                queue.append(i)
                visited[i] = True 
    return count

print(bfs(graph, 1, visited1))