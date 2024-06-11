# 2개 이하로 다른 비트 
# https://school.programmers.co.kr/learn/courses/30/lessons/77885

# x보다 크고 비트가 1~2개 다른 수 중 가장 작은 수 
# 처음 나오는 0에 대해 01 => 10으로 비트 변환 
# 비트 변환 후 첫자리가 0일 경우 +1 진행 

def int_ord(num1) : # 양의 정수 => 비트
    con_num1 = []
    while num1 : 
        con_num1.append((num1 % 2))
        num1 //= 2
        
    return [0] + con_num1[::-1]

def ord_int(list1) : # 비트 => 양의 정수 
    temp = 0
    count = 0
    for int1 in list1[::-1] : 
        temp += int(int1) * (2 ** count)
        count += 1
        
    return temp
        

def solution(numbers):
    answer = []
    for num in numbers : 
        temp = int_ord(num)[::-1]
        temp_0 = temp.index(0)
        if temp_0 : 
            temp[temp_0], temp[temp_0 - 1] = 1, 0
            
        else : 
            temp[temp_0] = 1
        
        answer.append(ord_int(temp[::-1]))

    return answer

# def solution(numbers):
#    answer = []
#    for idx, val in enumerate(numbers):
#        answer.append(((val ^ (val+1)) >> 2) + val +1)
#
#    return answer 

