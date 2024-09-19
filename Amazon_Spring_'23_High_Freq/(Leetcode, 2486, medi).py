# Append Characters to String to Make Subsequence
# https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/description
# Return the minimum number of characters to append to the end of string s so that t becomes a subsequence of s.

class Solution(object):
    def appendCharacters(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        cnt_s, cnt_t = 0, 0

        while cnt_s < len(s) :
            if s[cnt_s] == t[cnt_t] : 
                cnt_t += 1
                
                if cnt_t == len(t) : 
                    break
            
            cnt_s += 1

        return len(t) - cnt_t
        