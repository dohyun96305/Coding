# 당구 연습
# https://school.programmers.co.kr/learn/courses/30/lessons/169198

def solution(m, n, startX, startY, balls):
    
    answer = []
    
    for balls_x, balls_y in balls : 
        answer_temp = []
        
        # 만약 목표 공과 시작 공이 같은 선상 (x가 같거나 y가 같거나) 일 경우 조건 만족 X 
        
        if not (balls_x == startX and balls_y > startY) : # 위쪽 대칭이동
            answer_temp.append( (2 * n - startY - balls_y)**2 + (startX - balls_x) **2 )
        
        if not (balls_x == startX and balls_y < startY) : # 아래쪽 대칭이동
            answer_temp.append( (-1 * startY - balls_y)**2 + (startX - balls_x)**2 )

        if not (balls_y == startY and balls_x < startX) : # 왼쪽 대칭이동
            answer_temp.append( (-1 * startX - balls_x)**2 + (startY - balls_y)**2 )

        if not (balls_y == startY and balls_x > startX) : # 오른쪽 대칭이동
            answer_temp.append( (2 * m - startX - balls_x)**2 + (startY - balls_y)**2 ) 

        answer.append(min(answer_temp))
        
    return answer
        