# Spiral Matirx 2
# https://leetcode.com/problems/spiral-matrix-ii/description/ 
# 조건에 따른 방향 전환, List return

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """

        answer = [[0 for _ in range(n)] for _ in range(n)] # 전체 List
        dx = [0, 1, 0, -1] # 방향에 따른 x좌표 변화
        dy = [1, 0, -1, 0] # 방향에 따른 y좌표 변화

        nx, ny = 0, 0 # 현재 x, y 좌표
        k = 0 # 현재 방향 (0 : 오른쪽, 1 : 아래, 2 : 왼쪽, 3 : 위쪽)

        for i in range(1, n*n + 1) : 
            answer[nx][ny] = i # 현재 위치에 대해 번호 저장 

            kx = nx + dx[k%4] # 다음 x 좌표
            ky = ny + dy[k%4] # 다음 y 좌표 

            if (kx) < 0 or (kx) >= n or (ky) < 0 or (ky) >= n or answer[(kx)][(ky)] : 
                k += 1            
            # 다음 위치의 조건에 따른 방향 전환 
            # List를 넘거나 다음 위치에 이미 번호가 채워져있는 경우 방향 전환 

            nx += dx[k%4] # x 좌표 변화
            ny += dy[k%4] # y 좌표 변화 

        return answer

                