# 피로도 
# https://school.programmers.co.kr/learn/courses/30/lessons/87946
# k : 현재 피로도, 1 <= k <= 5000
# dungeons : 각 던전 별 [최소 피로도, 소모 피로도], 1 <= 각 피로도 <= 1000
# 완전 탐색, DFS 

answer = 0

def dfs(k, count, dungeons) : 
    global answer # answer 전역변수 선언
    if count > answer : 
        answer = count 
        
    for i in range(len(dungeons)) : 
        if k >= dungeons[i][0] and not visited[i] : 
            visited[i] = 1
            dfs(k-dungeons[i][1], count + 1, dungeons)
            visited[i] = 0 # visited 초기화를 통해 다음 DFS 확인

def solution(k, dungeons):
    global visited # visited 전역변수 선언 
    visited = [0] * len(dungeons)
    dfs(k, 0, dungeons)
    return answer