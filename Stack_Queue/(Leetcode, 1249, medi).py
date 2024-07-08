# Minimum Remove to Make Valid Parentheses
# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/description
# Given a string s of '(' , ')' and lowercase English characters, remove the minimum number of parentheses to make the string valid and return any resulting valid string.

class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_list = list(s) # To make string to list 
        temp = [] # Store index of '(', 

        for i in range(len(s)) : 
            if s[i] == '(' : 
                temp.append(i)

            elif s[i] == ')' : 
                if temp : 
                    temp.pop() # Making pair of '(', ')' available
                else : 
                    s_list[i] = '' # Not available => Need to remove
            
            else : 
                continue # pass of lowercase English string

        while temp : 
            s_list[temp.pop()] = '' # Rest of '(' need to remove

        return ''.join(s_list)
