# 배달 
# https://school.programmers.co.kr/learn/courses/30/lessons/12978
# 연결된 각 지점에 대해 1번에서 시작, K 거리 내 노드 개수 

def solution(N, road, K):
    answer = 0
    INF = 1e9
    
    graph = [[INF for _ in range(N+1)] for _ in range(N+1)]
    # 모든 연결 지점에 대한 정보 저장하는 graph list 생성 

    for i in range(1, N+1) : # 자기 자신의 거리 = 0
        graph[i][i] = 0
        
    for a, b, c in road : # 양방향 통행, 연결 및 거리 정보 저장 
        graph[a][b] = min(graph[a][b], c)
        graph[b][a] = min(graph[b][a], c)
    
    # 플로이드-위셜, O(n^3), N <= 50, 125,000 
    for a in range(1, N+1) : # 모든 연결 고리를 지나는 정보 확인 
        for b in range(1, N+1) : 
            for c in range(1, N+1) : 
                graph[b][c] = min(graph[b][c], graph[b][a] + graph[a][c])

    # K 거리 이전인 노드 개수 확인            
    for dist in graph[1] : 
        if dist <= K : 
            answer += 1
        
    return answer