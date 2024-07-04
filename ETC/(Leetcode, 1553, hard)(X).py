# Minimum Number of Days to Eat N oranges
# https://leetcode.com/problems/minimum-number-of-days-to-eat-n-oranges/description/
# Memory limited, Using Recursive Function 

# Three steps to eat Orange
# 1. eat 1 orange
# 2. eat 2*(n//3) orange when remain number of orange n => n%3 == 0
# 3. eat (n//2) orange when remain number of orange n => n%2 == 0

# DP or BFS

class Solution(object):
    cache = {0:0, 1:1, 2:2} # DP, For Memory Limited, Using self.cache
    # To refuse repeatedly calling same dict 

    def minDays(self, n):
        """
        :type n: int
        :rtype: int
        """
        # memorization of n => if n is in self.cache, using self.cache[n]
        # recursive function self.minDays()
        # n%3, n%2 => when eating 1 orange each day
        
        if n not in self.cache:
            self.cache[n] = 1 + min(self.minDays(n//3) + n%3, self.minDays(n//2) + n%2)
       
        return self.cache[n]
