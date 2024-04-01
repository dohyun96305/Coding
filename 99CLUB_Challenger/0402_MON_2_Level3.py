# 다단계 칫솔 판매
# https://school.programmers.co.kr/learn/courses/30/lessons/77486

from collections import deque
from math import ceil

def solution(enroll, referral, seller, amount):

    money_list = {a : 0 for a in enroll}
    graph_list = {a : b for a, b in zip(enroll, referral)} # child, parent 관계 확인
            
    for c, d in zip(seller, amount) :  
        queue = deque([c])
        money = d * 100
        
        while queue : 
            target = queue.pop()
        
            if money >= 1 and target != '-': 
                money_list[target] += ceil(money * 0.9) # 1원 미만 절삭
                money -= ceil(money * 0.9) 

                if graph_list[target] : 
                    queue.append(graph_list[target])
                
    return list(money_list.values())

