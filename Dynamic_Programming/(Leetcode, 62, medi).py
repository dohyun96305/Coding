# https://leetcode.com/problems/unique-paths/description/
# Unique Paths
# [0,0] -> [m-1][n-1] 까지의 최단 경로의 개수

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[1] * (n) for _ in range(m)] # dp 생성

        for i in range(1, m) : 
            for j in range(1, n) :
                dp[i][j] = dp[i-1][j] + dp[i][j-1] # 위에서 오는 경로 + 왼쪽에서 오는 경로

        return dp[m-1][n-1]

        
        