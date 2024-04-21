# 타겟 넘버 
# https://school.programmers.co.kr/learn/courses/30/lessons/43165
# 정수들을 더하거나 빼서 target value 만들 수 있는 횟수 

def dfs(idx, numbers, temp1, target) : # dfs 설정 
    global answer # 전역변수 설정 
    # 종료 조건
    if idx == len(numbers) : 
        if temp1 == target : 
            answer += 1
            return
        else :
            return 
        
    # 행동 조건 
    dfs(idx+1, numbers, temp1 + numbers[idx], target)
    dfs(idx+1, numbers, temp1 - numbers[idx], target)


def solution(numbers, target):
    global answer
    answer = 0
    dfs(0, numbers, 0, target)
    return answer


''' # 시간 자체는 빠름 
def solution(numbers, target):

    answer1 = [0]
    answer = 0
    
    for i in numbers : 
        temp = []
        
        for m in answer1 : 
            temp.append(m + i)
            temp.append(m - i)
            
        answer1 = temp
    
    return answer1.count(target)

'''