# Adding Spaces to String
# https://leetcode.com/problems/adding-spaces-to-a-string/description/
# Given a string s and an array spaces indicating indices where spaces should be inserted, return the modified string with spaces added at the specified positions.

# Time limited, Not 'for loop' for word length + not answer ''  

class Solution(object):
    def addSpaces(self, s, spaces):
        """
        :type s: str
        :type spaces: List[int]
        :rtype: str
        """
        answer = []
        temp = 0
        
        for idx in spaces : 
            answer.append(s[temp:idx])
            temp = idx

        answer += [s[temp:]]
        return ' '.join(answer)