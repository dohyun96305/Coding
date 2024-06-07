# 카운트 다운 
# https://school.programmers.co.kr/learn/courses/30/lessons/131129
# target까지 특정 조건을 통해 가장 적은 횟수로 도달할 수 있는 경우 Return

# 1~20점 + 50점, 1~3배수를 통해 가장 적은 횟수로 target value 도달 
# 횟수가 같을 경우 1배수 혹은 50점 횟수가 가장 많은 횟수로 Return 

# 1 ≤ target ≤ 100,000

def solution(target):
     
    dp = [[100000, 0] for _ in range(target+1)] # dp list 생성 (dp[i][0] => i점 도달에 필요한 라운드, dp[i][1] = i점 도달간 Single or Bull 횟수)
    dp[0][0] = 0 
    count = 0
    
    while target > 1000:
        target -= 60
        count += 1

    for i in range(target): # target 까지의 전체 점수
        for j in range(1, 21): # 1~20점
            # 갱신 조건 : 라운드 횟수가 적거나 (라운드 횟수가 같을 때 => Single or Bull 횟수가 많은 경우)
            
            if i+ j <= target and ( dp[i+ j][0] > dp[i][0] + 1 or (dp[i+ j][0] == dp[i][0] + 1 and dp[i+ j][1] < dp[i][1]+1) ):
                dp[i+j][0] = dp[i][0] + 1
                dp[i+j][1] = dp[i][1] + 1 # Single 인 경우 추가 
                
            if i+ 2*j <= target and ( dp[i+ 2*j][0] > dp[i][0] + 1 or (dp[i+ 2*j][0] == dp[i][0] + 1 and dp[i+ 2*j][1] < dp[i][1]) ):
                dp[i+ 2*j][0] = dp[i][0] + 1
                dp[i+ 2*j][1] = dp[i][1]
                
            if i+ 3*j <= target and ( dp[i+ 3*j][0] > dp[i][0] + 1 or (dp[i+ 3*j][0] == dp[i][0] + 1 and dp[i+ 3*j][1] < dp[i][1]) ):
                dp[i+ 3*j][0] = dp[i][0] + 1
                dp[i+ 3*j][1] = dp[i][1]
                
        if i+ 50 <= target and (dp[i+ 50][0] > dp[i][0]+1 or (dp[i+ 50][0] == dp[i][0]+1 and dp[i+ 50][1] < dp[i][1]+1)):
            dp[i+50][0] = dp[i][0] + 1
            dp[i+50][1] = dp[i][1] + 1 # Bull 인 경우 추가 

    dp[target][0] += count
    
    return dp[target]