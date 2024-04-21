# 부대복귀
# https://school.programmers.co.kr/learn/courses/30/lessons/132266
# 각 지역에서 도착점까지의 최소거리 return

# 지역 개수 n >= 100,000 => 다익스트라 기법 X
# 도착점에서 각 출발지역으로의 최소거리 구하는 문제 => BFS

from collections import deque

def solution(n, roads, sources, destination):
    graph_list = {k : [] for k in range(n+1)} # 연결 정보 저장 
    
    len_list = [-1] * (n+1) # 길이 정보 저장
    visited = [False] * (n+1) # 방문 정보 저장 
     
    for a, b in roads : 
        graph_list[a].append(b)
        graph_list[b].append(a)

    queue = deque([destination]) # bfs queue 생성 
    visited[destination] = True
    len_list[destination] = 0

    while queue : 
        now = queue.popleft()
        
        for k in graph_list[now] : # 연결되어있는 지역 
            if not visited[k] : 
                visited[k] = True 
                len_list[k] = len_list[now] + 1 # 연결된 지역들은 거리가 1
                queue.append(k)
    
    return [len_list[k] for k in sources]