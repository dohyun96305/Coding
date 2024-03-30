# 삼각 달팽이 
# https://school.programmers.co.kr/learn/challenges?order=acceptance_desc&levels=2&languages=python3&page=1&search=%EC%82%BC%EA%B0%81
# 삼각형 모양으로 숫자를 배열하는 문제

def solution(n):
    answer = []
    answer_triangle = [[0] * i for i in range(1, n+1)] 

    turn = [[1, 0], [0, 1], [-1, -1]] # 각 조건에 따른 x, y 변화
    
    num_answer = (n**2 + n) //2 
    count_plus = 0
    
    k = 0
    x, y = 0, 0
    count = 0
    
    for i in range(1, num_answer+1) : 
        answer_triangle[x][y] = i
        count += 1
        
        if count % n == 0 : 
            if k == 2 : 
                k = 0
            else : 
                k += 1
            
            count_plus += 1
            count = count_plus
            
        x, y = x + turn[k][0], y + turn[k][1]  
        
    for row in answer_triangle : 
        answer += row
        
    return answer
