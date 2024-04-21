# 문자열 나누기 
# https://school.programmers.co.kr/learn/courses/30/lessons/140108
# 특정 조건을 통해 단어를 분해하는 문제 

def solution(s):
    answer = 0
    
    while len(s) > 0 :
        count1 = 0 # 전 글자와 현 글자가 같은 횟수
        count2 = 0 # 전 글자와 현 글자가 다른 횟수
        st = s[0] # 기준 단어의 첫 글자
        lt = len(s) # 기준 단어의 길이
        
        for i, k in enumerate(s) : 
            if k == st : 
                count1 += 1
            else : 
                count2 += 1
            
            if count1 == count2 : 
                answer += 1
                s = s[i + 1 : ]
                break
        
        if lt == len(s) :
            return answer + 1 # 더 이상 조건을 만족하지 않는 경우
            
    return answer