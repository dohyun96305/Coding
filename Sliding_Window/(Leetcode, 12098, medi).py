# Get Equal Substrings Within Budget
# https://leetcode.com/problems/get-equal-substrings-within-budget/description
# Return the maximum length of a substring in s that can be changed to match t with a cost ≤ maxCost.

class Solution(object):
    def equalSubstring(self, s, t, maxCost):
        """
        :type s: str
        :type t: str
        :type maxCost: int
        :rtype: int
        """

        temp = 0
        
        min_ind = 0 # Left index
        max_length = 0 # Max length of substring

        for max_ind in range(len(s)) :
            maxCost -= abs( ord(t[max_ind]) - ord(s[max_ind]) ) 
            temp += 1
            
            while maxCost < 0 : # If maxCost < 0, make min_ind += 1
                maxCost += abs( ord(t[min_ind]) - ord(s[min_ind]) )
                min_ind += 1
                temp -= 1

            max_length = max(max_length, temp) # Updating max_length

        return max_length 