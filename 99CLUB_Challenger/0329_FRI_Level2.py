# 점 찍기
# https://school.programmers.co.kr/learn/courses/30/lessons/140107
# k : 점 찍는 위치의 배수, 1 <= k <= 1000000
# d : 원점과의 거리, 1 <= d <= 1000000 

def solution(k, d) : 
    answer = 0
    target = d**2 # 원점과의 거리 제곱합, x**2 + y**2 <= d**2 만족
    
    for x in range(0, d+1, k) : # x 좌표 
        y = int((target - x**2)**(1/2)) // k # y 좌표, 위 조건을 만족하는 최대값 // k => x 좌표에 따른 y 좌표 개수  
        
        answer += y
        answer += 1 # y 좌표가 0인 경우
        
    return answer 
