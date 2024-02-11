# https://leetcode.com/problems/min-cost-climbing-stairs/description
# Min Cost Climbing Stairs
# 해당 층에서 올라갈 때 cost를 지불, 한 번에 1칸 혹은 2칸 올라감, 최소 비용 return 

class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        
        dp = [0] * ( len(cost) + 1 ) # 출발점 cost 0, dp 생성

        for i in range(1, len(cost)) : 
            dp[i+1] = min(dp[i-1] + cost[i-1], dp[i] + cost[i])
            # i+1 층 => min(i-1층까지의 dp + i-1층의 cost, i층까지의 dp + i층의 cost)

        return dp[-1] # 마지막 층 값 => min 값 return