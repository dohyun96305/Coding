# Number of Ways to Select Buildings
# https://leetcode.com/problems/number-of-ways-to-select-buildings/description
# Return the number of valid ways to select 3 buildings from a binary string where no two consecutive buildings have the same type.

# s[i] = 0 => office, s[i] = 1 => restaurant
# select 3 buildings for random , no 2 consecutive can be same type
# return number of vaild ways to select

# dp 
# 001101
# two type of buildings => "010", "101"

class Solution(object):
    def numberOfWays(self, s):
        """
        :type s: str
        :rtype: int
        """
        counts_0, counts_1 = 0, 0
        counts_01, counts_10 = 0, 0
        counts_010, counts_101 = 0, 0

        for i, v in enumerate(s):
            if v == '0':
                counts_0 += 1
                counts_10 += counts_1
                counts_010 += counts_01   
                      
            else:
                counts_1 += 1
                counts_01 += counts_0
                counts_101 += counts_10

        return counts_010 + counts_101

answer = Solution()
print(answer.numberOfWays("001101"))