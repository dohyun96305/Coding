# 단어 변환
# https://school.programmers.co.kr/learn/courses/30/lessons/43163
# BFS, DFS 문제 
# 단어간 한글자 변환을 통해 begin => target 최소 변환 횟수 return 

from collections import deque

def solution(begin, target, words):

    words = [begin] + words
    graph = {x : [] for x in words} # 연결된 단어 저장
    visited = {x : False for x in words} # 방문 확인
      
    if target not in words : # 없을시 종료
        return 0
    
    for i in words : # 단어간 연결 확인 (한 글자만 다른 경우 연결)
        for j in words : 
            words_len = 0
            
            if i == j : # 똑같으면 통과
                continue
                
            else : 
                for a, b in zip(i, j) : 
                    if a == b : 
                        words_len += 1
                        
                if words_len == len(i) -1 : 
                    graph[i] += [j]
    
    queue = deque()
    queue.append((begin, 0))
    
    while queue : 
        parent, answer = queue.popleft()
        visited[parent] = True # 방문 처리 
        
        for child in graph[parent] : 
            if child == target : 
                return answer + 1
            
            else : 
                if not visited[child] : 
                    queue.append((child, answer+1))
    
