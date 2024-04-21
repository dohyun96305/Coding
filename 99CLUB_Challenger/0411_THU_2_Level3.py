# 인사고과
# https://school.programmers.co.kr/learn/courses/30/lessons/152995

# 두 점수 모두 낮은 경우 인센티브 수령 제외 
# 두 점수 합 클수록 높은 순위 
# 순위가 같을 경우 그만큼 다음 순위는 넘어감 

def solution(scores):
    answer = 0
    answer_score = [scores[0][0], scores[0][1], sum(scores[0])]
    max_b = 0
    
    scores_sort = sorted(scores, key = lambda x : (-x[0], x[1])) 
    # 근무태도가 높은 순대로 정렬, 같다면 동료 평가 점수가 낮은 순대로
    # 어쩃든 근무태도는 작은 상태, 동료 평가 점수 비교를 통해 조건 확인
    
    for a, b in scores_sort : 
        if a > answer_score[0] and b > answer_score[1] : # 모두 작다면 인센티브 대상 X 
            return -1
        
        if b >= max_b : 
            max_b = b
            if a+b > answer_score[2] : 
                answer += 1

    return answer + 1

