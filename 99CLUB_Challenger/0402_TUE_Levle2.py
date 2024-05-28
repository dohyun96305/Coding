# 택배상자
# https://school.programmers.co.kr/learn/courses/30/lessons/131704
# 택배를 순서대로 전달, 전달 가능한 상자의 숫자 

def solution(order):
    belt = []
    i = 1
    cnt = 0 
    
    while i != len(order)+1:
        belt.append(i)
        
        while belt and belt[-1] == order[cnt]:
            cnt += 1
            belt.pop()
            
        i += 1
        
    return cnt