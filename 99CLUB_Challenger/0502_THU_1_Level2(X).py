# 조이스틱 
# https://school.programmers.co.kr/learn/courses/30/lessons/42860
# 문자열 만들기 위한 최소 이동횟수 (알파벳 만들기 + 좌우로 움직이기)

# https://velog.io/@jqdjhy/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%A1%B0%EC%9D%B4%EC%8A%A4%ED%8B%B1-Greedy
# 시각적 참고 
# 좌우로 움직이는 횟수에 대한 조건 

def solution(name):
    answer = 0

    # 좌우 움직이는 최소 횟수 : 왕복 없이 한쪽 방향으로만 이동 
    min_lr = len(name) - 1
    
    for i, s in enumerate(name) :
        # 위, 아래 움직이는 횟수는 고정되어 있음 (위, 아래 움직이는 횟수 중 최솟값)
        answer += min(ord('Z') - ord(s) + 1, ord(s) - ord('A'))
        next1 = i+1

        # 현재 글자 기준, 다음 글자 확인 했을 때 연속된 A인지 확인 
        while next1 < len(name) and name[next1] == 'A' : 
            next1 += 1
        
        # 연속된 A에 대해서 좌우로 움직이는 횟수의 최솟값 갱신 
        min_lr = min(min_lr, 2*i + len(name) - next1, i + 2*(len(name) - next1))

    # 좌우로 움직이는 최솟값 추가 
    answer += min_lr

    return answer