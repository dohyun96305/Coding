# 우박수열 정적분 
# https://school.programmers.co.kr/learn/courses/30/lessons/134239
# 홀수, 짝수에 따른 조건 - 그래프 밑 넓이 

def solution(k, ranges):
    answer = []
    answer1 = []
    answer2 = []
    temp = []
    x = 0
    
    while k != 1 : 
        answer1.append([x,k])
        
        if k % 2 == 0 : 
            k = k//2
        else : 
            k = k*3 + 1
        
        x += 1
    
    answer1 = answer1 + [[x,k]]
    
    for a in range(len(answer1)-1) : 
        answer2.append((answer1[a][1] + answer1[a+1][1])/2)
            
    for a, b in ranges : 
        answer.append(sum(answer2[a:x+b]) if a <= x+b else -1)
        
    return answer