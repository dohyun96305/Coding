# https://leetcode.com/problems/is-subsequence/description
# Is Subsequence
# 두 문자열 s, t에 대해 s가 t의 subsequence인지 확인

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i = 0 # s의 pointer i, 순서의 기준
        
        if not s : 
            return True 

        for j in range(len(t)) : # O( len(t) ),  t의 pointer j 
            if t[j] == s[i] :  # 순서를 만족하며 s의 문자열과 동일할때 
                i += 1

            if i == len(s) : # 조건을 만족한다면 뒤는 볼 필요 X
                return True

        return False 
                

        