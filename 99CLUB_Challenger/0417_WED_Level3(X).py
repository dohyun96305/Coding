# 미로 탈출 명령어 
# https://school.programmers.co.kr/learn/courses/30/lessons/150365
# 시작점에서 도착점까지 k횟수를 통해 이동한 경로 중 사전순으로 제일 빠른 경로 return

# DFS 문제 => 사전순에서 빠른 순대로 DFS 진행, 경로 return 

import sys
sys.setrecursionlimit(10**5)

def solution(n, m, x, y, r, c, k):
    
    # 총 거리 dist
    dist = abs(x - r) + abs(y - c)
    
    # 예외처리
    if dist > k : # dist가 k보다 클 경우 예외
        return 'impossible'
    
    if dist % 2 is not k % 2 : # dist + 짝수 = k 를 만족 => (홀, 홀) or (짝, 짝) 만족해야함 
        return 'impossible'
    
    move = ['d', 'l', 'r', 'u'] # 사전순
    dx = [1, 0, 0, -1]
    dy = [0, -1, 1, 0]
    
    def dfs(cx, cy, path, cnt) : 
        if cnt == k : # dist == k일 경우
            if cx == r and cy == c : # 좌표가 도착점과 일치할 경우
                return path
            
        else : 
            for i in range(4) : # 사전순으로 반복문 진행
                nx = cx + dx[i]
                ny = cy + dy[i]
                
                # 미로 좌측 상단 (1, 1), 우측 하단 (n, m)
                if 1 <= nx <= n and 1 <= ny <= m : # 격자 안에 있을 경우
                    dist = abs(nx - r) + abs(ny - c) # 현재로부터 남은 거리

                    if dist > k - (cnt + 1) : # 현재 남은 거리가 남은 횟수보다 길 경우 예외
                        continue

                    dfs_plus = dfs(nx, ny, path + move[i], cnt + 1)

                    if dfs_plus is not None : # 최종 path까지의 return 확인 
                        return dfs_plus

    answer = dfs(x, y, '', 0)
    
    if answer is None : 
        return 'imposible'
    
    return answer
