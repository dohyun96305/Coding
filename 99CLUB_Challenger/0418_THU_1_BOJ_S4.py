# 균형잡힌 세상 
# https://www.acmicpc.net/problem/4949
# 주어진 문자열에 대해 괄호의 균형 확인 후 return 

while True : 
    sentences = input()

    if sentences == '.' : 
        break
        
    else : 
        num_a = 0
        num_b = 0
        left_list = []

        for i in sentences : 
            if i == '(' or i == '[' : 
                left_list.append(i)

            elif i == ')' : 
                if left_list and left_list[-1] == '(' : 
                    left_list.pop()
                else : 
                    left_list.append(i)
                    break
            
            elif i == ']' : 
                if left_list and left_list[-1] == '[' : 
                    left_list.pop()
                else : 
                    left_list.append(i)
                    break

        if left_list : 
            print('no')
        else : 
            print('yes')