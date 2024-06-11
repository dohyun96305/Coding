# 억억단을 외우자 
# https://school.programmers.co.kr/learn/courses/30/lessons/138475
# starts 리스트내 양의 정수 s에 대해 s보다 크거나 같고 e보다 작거나 같은 약수의 개수가 가장 많은 수 return

# 약수의 개수 구하는 공식 중요 (시간 복잡도 감소)
# 다시 보자 

def solution(e, starts):
    
    answer = []
    divisor = [0 for _ in range(e + 1)]
    divisor_index = [0 for _ in range(e + 1)]
    
    ##### 약수의 개수 구하는 공식 (시간 복잡도 감소)
    for i in range(2, e + 1):
        for j in range(1, min(e//i + 1, i)): # 약수 곱하기 +2
            divisor[i * j] += 2
            
    for i in range(1, int(e**(1/2)) + 1): # 제곱수 곱하기 +1
        divisor[i ** 2] += 1
    #####
    
    max_count = 0

    for i in range(e, 0, -1):
        if max_count <= divisor[i]:
            max_count, divisor_index[i] = divisor[i], i
            
        else:
            divisor_index[i] = divisor_index[i + 1]

    for i in starts:
        answer.append(divisor_index[i])
        
    return answer