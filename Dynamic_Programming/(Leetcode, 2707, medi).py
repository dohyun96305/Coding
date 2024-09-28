# Extra Characters in String 
# https://leetcode.com/problems/extra-characters-in-a-string/description

# Given a string s and a dictionary of words, break s into substrings from the dictionary, 
# leaving as few extra characters as possible, and return the minimum number of leftover characters.

# First => Dynamic Programming
# Second => Recursive with Memorization

class Solution(object):
    def minExtraChar(self, s, dictionary):
        """
        :type s: str
        :type dictionary: List[str]
        :rtype: int
        """
        dp = [0] + [float('inf')] * (len(s))
        wordSet = set(dictionary)
        
        for i in range(1, len(s)+1) :
            dp[i] = dp[i-1] + 1

            for j in range(0, i) :
                if s[j : i] in wordSet :
                    dp[i] = min(dp[i], dp[j])
                    
        return dp[-1]
    

'''
        def find(s, memo):
            if s in memo:
                return memo[s]

            if not s:
                return 0

            extra1, extra2 = inf, inf

            for word in dictionary:
                if word == s[:len(word)]:
                    extra1 = min(extra1, find(s[len(word):], memo))

            extra2 = find(s[1:], memo) + 1 
            memo[s] = min(extra1, extra2)
            
            return memo[s]

        return find(s, {})
'''
answer = Solution()
print(answer.minExtraChar("dwmodizxvvbosxxw", ["ox","lb","diz","gu","v","ksv","o","nuq","r","txhe","e","wmo","cehy","tskz","ds","kzbu"]))
