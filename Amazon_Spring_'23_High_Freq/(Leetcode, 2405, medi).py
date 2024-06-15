# Optimal Partition of String
# https://leetcode.com/problems/optimal-partition-of-string/?envType=study-plan-v2&envId=amazon-spring-23-high-frequency
# Given string S, partition S substrings such that the characters in each substring are unique

class Solution(object):
    def partitionString(self, s):
        """
        :type s: str
        :rtype: int
        """
        last_word = set()
        answer = 1

        for i in s : 
            if i in last_word  :
                last_word = set()
                answer += 1

            last_word.add(i)

        return answer 


        