import heapq
from math import inf

# 등산코스 정하기 
# https://school.programmers.co.kr/learn/courses/30/lessons/118669
# 다익스트라 => 우선순위 heapq를 통한 문제 

def solution(n, paths, gates, summits):

    graph = [[] for _ in range(n + 1)] # graph 생성, 양방향
    for i, j, w in paths:
        graph[i].append([j, w])
        graph[j].append([i, w])

    is_summit = [False] * (n + 1) # 산봉우리 정보 저장 
    for summit in summits:
        is_summit[summit] = True

    distance = [inf] * (n + 1) # 길이 정보 + 출입구 저장 (distance 0을 통한 heapq 우선순위)
    queue = []
    for gate in gates:
        distance[gate] = 0
        heapq.heappush(queue, [0, gate])

    # 다익스트라
    while queue:
        d, i = heapq.heappop(queue)

        if distance[i] < d or is_summit[i]: # 산봉우리 도착 시 continue
            continue
            
        for j, dd in graph[i]:
            dd = max(distance[i], dd)
            
            if distance[j] > dd:
                distance[j] = dd
                heapq.heappush(queue, [dd, j])
                print(heapq)


    result = [-1, inf] # 결과 출력 [산봉우리, 거리]
    for summit in sorted(summits):
        if distance[summit] < result[1]:
            result[0] = summit
            result[1] = distance[summit]
            
    return result