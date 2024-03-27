# 마법의 엘리베이터 
# https://school.programmers.co.kr/learn/courses/30/lessons/148653

# storey : 현재 층수, 1 ≤ storey ≤ 100,000,000

def solution(storey):
    answer = 0
    temp = 0 # 10이 넘어갈 때 +1 용도
    number_length = len(str(storey)) - 1
    number_reverse_str = str(storey)[::-1]
    
    for a, i in enumerate(number_reverse_str) : 
        number = int(i) + temp
        
        if number > 5 : # 만약 5 초과일 경우 10 맞추는 것이 이득
            answer += 10 - number
            temp = 1
            
            if a == number_length : # 마지막 자리수 처리
                answer += 1 
                break
                
        elif number == 5 : # 만약 5일 경우 다음 자리 수 확인
            if a == number_length : 
                answer += 5
                break
                
            else : 
                if int(number_reverse_str[a+1]) <= 4 : # 다음 자리 수 + 1이 5가 넘지 않을 경우
                    answer += number
                    temp = 0
                    
                else : # 다음 자리 수 + 1이 5가 넘을 경우
                    answer += (10 - number)
                    temp = 1
            
        else : # 만약 5미만 일 경우 0 맞추는 것이 이득 
            answer += number
            temp = 0

    return answer