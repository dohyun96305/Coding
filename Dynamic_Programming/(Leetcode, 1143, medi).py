# https://leetcode.com/problems/longest-common-subsequence/
# Longest_Common_Subsequence
# text1 내 text2의 연속적인 가장 긴 문자열의 길이 반환 

class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        l1 = len(text1)
        l2 = len(text2)
        
        dp = [[0] * (l2+1) for _ in range(l1+1)] # text1-text2 길이에 따른 DP 생성

        for i in range(l1) : # Time Complexity : O(l1*l2)
            for j in range(l2) : 
                if text1[i] == text2[j] : # text1[i], text2[j]의 문자열이 같을 경우 
                    dp[i][j] = dp[i-1][j-1] + 1 # 전 상황에서의 값 +1

                else : # text1[i], text2[j]의 문자열이 다를 경우 
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1]) # 전 상황에서의 값 중 최댓값 반환

        return dp[i][j] # 마지막 값이 최대의 값
        
        