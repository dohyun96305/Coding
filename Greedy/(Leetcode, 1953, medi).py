# https://leetcode.com/problems/maximum-number-of-weeks-for-which-you-can-work/description/
# Maximum Number of Weeks for Which You Can Work
# 연속되지 않게 n개의 프로젝트의 작업량 할당
# milestones = [1,2,3,4,5]

# --------------------------------------------------------------------------------------
# max(milestones)를 기준으로 문제를 해결  

# max(milestones) = 5 => X O X O X O X O X O X
# X 6개 자리에 나머지 milestones (= temp = sum - max)를 배치

# 만약 temp >= max : 
#   temp 사이사이에 max가 다 들어갈 수 있다
#   결국 모든 milestones가 연속되지 않음 => temp + max = sum

# 만약 temp < max : 
#   최대한 max를 남기면서 temp를 배치
#   결국 max가 하나 남으면서 나머지 temp * 2 만큼 배치 => temp * 2 + 1

# 존재하는 경우의 수의 종류를 하나의 덩어리로 보면서 일반화? 

# -------------------------------------------------------------------------------------
# greedy 알고리즘 
# 여러 경우 중 하나를 결정할 떄 최적이라고 생각되는 것을 선택하면서 최종적인 해답에 도달
# 1. 선택 : 현재 상태에서 최적의 해답을 선택
# 2. 적절성 : 선택된 해답이 문제의 조건을 만족하는지 검사
# 3. 해답 : 최종 해결 방법인지 검사하고 아니라면 위의 과정 반복 

# 최적 부분 구조를 만족 
# => 문제의 최종 해결 방법은 부분 문제에 대한 최적 문제 해결 방법으로 구성

class Solution(object):
    def numberOfWeeks(self, milestones):
        """
        :type milestones: List[int]
        :rtype: int
        """

        temp = sum(milestones) - max(milestones)
        
        if temp >= max(milestones) : 
            return temp + max(milestones)

        else : 
            return temp * 2 + 1
