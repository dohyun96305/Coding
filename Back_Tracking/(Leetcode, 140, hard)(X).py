# Word Break II
# https://leetcode.com/problems/word-break-ii/description
# Given a string s and a dictionary wordDict, return all possible sentences formed by adding spaces in s such that each word is a valid dictionary word, allowing reuse of dictionary words.

# Back_Tracking
# Same word in the wordDict may be reused multiple times

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        answer = []
        wordDict = set(wordDict)

        def backtrack(i, start, current) : # BackTracking, Recursive Function
            if i == len(s) : 
                if len(''.join(current)) == len(s) : # If all words in S is used => return 
                    answer.append(' '.join(current)) # answer 

                return

            backtrack(i+1, start, current)

            if s[start : i+1] in wordDict : # To check word in wordDict
                current.append(s[start : i+1]) # Cuurent 
                backtrack(i+1, i+1, current)
                current.pop() # BackTrack, 

        backtrack(0, 0, [])

        return answer        