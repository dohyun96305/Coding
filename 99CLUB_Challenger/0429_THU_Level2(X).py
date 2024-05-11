# 하노이의 탑
# https://school.programmers.co.kr/learn/courses/30/lessons/12946
# 유명한 문제, 재귀함수 

def hannoi(n, start, end, yebi, answer) : 
    if n == 1 : 
        answer.append([start, end])
        return 
    
    hannoi(n-1, start, yebi, end, answer)
    # 가장 큰 원판 제외 나머지를 yebi 판으로 
    answer.append([start, end])
    # 제일 큰 원판을 end로
    hannoi(n-1, yebi, end, start, answer)
    # 나머지 원판을 end로
    
def solution(n):
    answer = []
    hannoi(n, 1, 3, 2, answer)
    return answer