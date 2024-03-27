# https://leetcode.com/problems/house-robber/description
# House Robber
# 연속된 두 개를 도둑질 할 수 없음, 이득 최댓값

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums : # 예외 처리 먼저 (1)
            return 0

        if len(nums) == 1 : # 예외 처리 먼저 (2) 
            return nums[0]

        dp = [0] * (len(nums) + 1) # dp 행렬 
        dp[1] = nums[0]  # 초기값 설정, 예외 처리하고 초기값 설정
   
        for i in range(1, len(nums)) : 
            dp[i+1] = max(dp[i], dp[i-1] + nums[i]) # 전 위치, 전 전 위치 + 현재 위치 최댓값이 그 자리 최댓값

        return dp[len(nums)]