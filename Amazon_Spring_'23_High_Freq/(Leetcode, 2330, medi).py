# Valid Palindrome IV
# https://leetcode.com/problems/valid-palindrome-iv
# Check if string s can be made a palindrome with exactly one or two character changes.

class Solution(object):
    def makePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        start, end = 0, (len(s) - 1) # Set two pointers
        count = 0 # For check count of changes

        while start <= end : 
            if s[start] != s[end] : # Count check
                count += 1

            if count > 2 : # If count of changes > 2 => return False  
                return False
            
            start += 1
            end -= 1

        return True