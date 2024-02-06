# https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/description
# Nearest Exit from Entrance in Maze
# 미로에서 밖으로 나갈 수 있는 최소 거리수 

from collections import deque

class Solution(object):
    def nearestExit(self, maze, entrance):
        """
        :type maze: List[List[str]]
        :type entrance: List[int]
        :rtype: int
        """
        sx, sy = entrance # 시작점
        maze[sx][sy] = 0 # 시작점 초기화, 갔다가 돌아오는 방법 X

        dx = [-1,1,0,0]
        dy = [0,0,-1,1]

        n = len(maze) # maze 끝 점 확인
        m = len(maze[0]) # maze 끝 점 확인

        queue = deque()
        queue.append([sx, sy]) # queue 생성 및 시작점 지정

        while queue : 
            x, y = queue.popleft()

            for i in range(4) : # 좌, 우, 위, 아래 이동 
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == '.' : # 미로 안에 있고 갈 수 있는 구간일 때
                    if nx == 0 or nx == n-1 or ny == 0 or ny == m-1 :  # 그 위치가 미로의 끝점, 즉 출구라면 
                        return maze[x][y] + 1 # 현재 거리 + 1 => 출구까지의 최소 거리 

                    queue.append([nx, ny])
                    maze[nx][ny] = maze[x][y] + 1 

        return -1

        