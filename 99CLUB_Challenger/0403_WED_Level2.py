# 무인도 여행
# https://school.programmers.co.kr/learn/courses/30/lessons/154540

from collections import deque

def bfs(maps, visited, list1) : 
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        
        n = len(maps)
        m = len(maps[0])
        
        queue = deque([list1]) 
        answer_temp = 0
        
        while queue : 
            x, y = queue.popleft()
            answer_temp += int(maps[x][y])
            visited[x][y] = True
                
            for i in range(4) : 
                nx = x + dx[i]
                ny = y + dy[i]
                
                if nx < 0 or nx >= n or ny < 0 or ny >= m : 
                    continue
                
                if not visited[nx][ny] and maps[nx][ny] != 'X' : 
                    queue.append([nx, ny])
                    visited[nx][ny] = True
                    
        return answer_temp
    
def solution(maps):
    answer = []
    
    n = len(maps)
    m = len(maps[0])
    
    visited_list = [[False] * m for _ in range(n)]
    
    for i in range(n) : 
        for j in range(m) : 
            if maps[i][j] != "X" and not visited_list[i][j]  : 
                answer.append(bfs(maps, visited_list, [i, j]))
                
    return sorted(answer) if answer else [-1]