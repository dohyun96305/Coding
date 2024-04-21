# 풍선 터뜨리기 
# https://school.programmers.co.kr/learn/courses/30/lessons/68646

# 기본적으로 인접한 풍선 2개 중 번호가 더 큰 풍선을 터트린다
# 번호가 큰 풍선만을 터뜨린다면 전체 중 결국 가장 작은 풍선만 남게 된다. 

# 조건을 통해 한번 번호가 작은 풍선을 터뜨릴 수 있음 
# 번호가 더 작은 풍선을 터트리는 행위는 최대 1번 
# 각 풍선의 양쪽에서의 최소의 풍선들중 하나보다만 작다면 남을 수 있다.
# 양쪽 끝은 확정적으로 남을 수 있음.

def solution(a):
    if len(a) == 1:
        return 1

    answer = 2   # 기본적으로 양쪽 끝은 끝까지 살아남을 수 있음
    
    # 최솟값 쌓기 ----------------
    l_min = [a[0]] # 각 풍선 왼쪽의 최소 풍선 저장
    r_min = [a[-1]] # 각 풍선 오른쪽의 최소 풍선 저장  
    
    for i in range(1, len(a)): # 각 풍선별 양쪽 최소 풍선 리스트 저장 
        if a[i] < l_min[-1]:
            l_min.append(a[i])
        else:
            l_min.append(l_min[-1])
            
        if a[len(a) - 1 - i] < r_min[-1]: 
            r_min.append(a[len(a) - 1 - i])
        else:
            r_min.append(r_min[-1])
            
    r_min.reverse()    
    # -----------------
    
    print(l_min)
    print(r_min)

	# 찾은 최솟값으로 비교 계산 -------------
    for i in range(1, len(a) - 1): # 양쪽 끝 제외 각 풍선별 조건 비교
        if l_min[i - 1] > a[i] or r_min[i + 1] > a[i]:
            answer += 1
    # --------------------------------
            
    return answer


