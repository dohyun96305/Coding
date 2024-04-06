# 디펜스 게임 
# https://school.programmers.co.kr/learn/courses/30/lessons/142085#
# heapq 문제

import heapq

def solution(n, k, enemy):
    answer = 0
    heap = []
    
    for i in enemy : 

        heapq.heappush(heap, -i) # heapq 사용, heappop간 최댓값 사용 위해 -1
        n -= i
        
        if n < 0 : # 병사의 수보다 적의 수가 많을 때
            if k > 0 : # 기회가 남아있을 때
                a1 = heapq.heappop(heap)
                n += (-1 * a1) # 복구
                k -= 1  # 기회 -1
                
            else : 
                break # 반복문 중지

        answer += 1 # count + 1
            
    return answer

