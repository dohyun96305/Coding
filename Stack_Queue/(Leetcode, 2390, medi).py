# https://leetcode.com/problems/removing-stars-from-a-string/description
# Removing Stars From a String
# 문자열 s에 *의 유무에 따른 조건문 수행

from collections import deque

class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        temp = deque() 
        
        for i in s : 
            if i == '*' : 
                temp.pop()
            else : 
                temp.append(i)
        
        return ''.join(temp)
        