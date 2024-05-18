# 공 이동 시뮬레이션 
# https://school.programmers.co.kr/learn/courses/30/lessons/87391
# 격자내 공 이동, 시작점에서 목표지점까지 갈 수 있는 시작점 개수 

# 시작점의 개수가 너무 많음 => 시간초과 
# 목표지점에서 이동에 대해 반대로 수행, 가능한 범위를 확인 
# n, x = 행, m, y = 열 

def solution(n, m, x, y, queries):
    answer = 0
    lx, rx, uy, dy = y, y, x, x # 최초 위치 : 목표지점 - 행, 열에 대한 최소, 최대
    queries.reverse() # queries에 대해 순서 및 방향을 반대로 확인 
    
    for dire, dx in queries : 
        if dire == 0 : # 왼쪽 => 오른쪽 
            temp = (rx + dx) if (rx + dx) < m else m-1 
            if lx == 0 : rx = temp 
            else : lx, rx = lx + dx, temp 
            
        if dire == 1 : # 오른쪽 => 왼쪽
            temp = (lx - dx) if (lx - dx) >= 0 else 0
            if rx == m-1 : lx = temp
            else : lx, rx = temp, rx - dx
            
        if dire == 2 : # 위쪽 => 아래쪽
            temp = (dy + dx) if dy + dx < n else n-1
            if uy == 0 : dy = temp
            else : uy, dy = uy + dx, temp
            
        if dire == 3 : # 아래쪽 => 위쪽
            temp = (uy - dx) if uy - dx >= 0 else 0
            if dy == n-1 : uy = temp
            else : uy, dy = temp, dy - dx
            
        if uy > n-1 or dy < 0 or lx > m-1 or rx < 0 : # 목표지점에서 움직였을 때, 위치 불가능한 곳 => 이동 불가 => 시작점 개수 = 0
            return 0
    
    answer = (rx - lx + 1) * (dy - uy + 1) # 갈 수 있는 시작점 범위에 대해 점 개수 구하기 
    
    return answer

# n행 m열 격자 
# query 4개 => 위, 아래, 왼쪽, 오른쪽 dx칸 만큼
# 0 => 왼, 1 => 오, 2 => 위, 3 => 아
# 0 => 오, 1 => 왼, 2 => 아, 3 => 위 

# 격자 밖으로 이동할 수 없음, 이동하고 마지막에 멈춤
# 모든 시작점에 대해 (x, y)에 도착하는 경우의 수 

# 모든 경우를 판단할 수는 없음 : 시간초과 
# queries 에서의 방향을 통해 확인 