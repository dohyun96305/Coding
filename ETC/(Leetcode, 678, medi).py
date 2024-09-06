# Valid Parenthesis String
# https://leetcode.com/problems/valid-parenthesis-string/description
# To determine if a string containing '(', ')', and '' is valid, ensure that each '(' has a matching ')', the parentheses are correctly ordered, and treat '' flexibly as '(', ')', or an empty string.

class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left_temp = []
        star_temp = []
        
        for i, str1 in enumerate(s) :   # Check str1 and index 
            if str1 == '(' : 
                left_temp.append(i)     

            elif str1 == ')' : 
                if left_temp : 
                    left_temp.pop()     

                elif star_temp : 
                    star_temp.pop()

                else : 
                    return False
            
            else : 
                star_temp.append(i)

        while left_temp and star_temp : 
            if left_temp.pop() > star_temp.pop() : 
                return False

        return not left_temp  