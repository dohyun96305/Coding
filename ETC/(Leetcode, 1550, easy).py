# Three Consecutive Odds
# https://leetcode.com/problems/three-consecutive-odds/
# Return True if three consecutive odd numbers in the arr

class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        count = 0
        for a in arr : 
            if a % 2 == 0 : 
                count = 0

            else : 
                count += 1
                if count == 3 : 
                    return True

        return False
        