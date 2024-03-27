# 다리를 지나는 트럭
# https://school.programmers.co.kr/learn/courses/30/lessons/42583

# bridge_length : 다리에 올라갈 수 있는 트럭 수, 1 <= bridge_length <= 10000
# weight : 다리가 견딜 수 있는 무게, 1 <= weight <= 10000
# truck_weights : 트럭 별 무게, 1 <= truck_weights <= weight

from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    bridge = [0] * bridge_length 
    bridge = deque(bridge) 
    truck_weights = deque(truck_weights)
    bridge_weights = 0
    
    while truck_weights : 
        answer += 1 # 시간 체크 
        k1 = bridge.popleft() # 다리 건너감
        bridge_weights -= k1 # 무게 빠짐 
        
        if bridge_weights + truck_weights[0] <= weight : # 다음 트럭이 무게 미만일 경우 
            k = truck_weights.popleft() 
            bridge.append(k)
            bridge_weights += k
            
        else : # 다음 트럭이 무게 초과할 경우
            bridge.append(0)
            
    answer += bridge_length
        
    return answer