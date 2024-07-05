# Decode the Slanted Ciphertext
# https://leetcode.com/problems/decode-the-slanted-ciphertext/description/
# Given an encoded string encodedText and a number of rows, determine the original string originalText that was encoded using a slanted transposition cipher.

# Careful when idx of encodedText is out of index

class Solution(object):
    def decodeCiphertext(self, encodedText, rows):
        """
        :type encodedText: str
        :type rows: int
        :rtype: str
        """
        if rows == 1 : # Exception cases
            return encodedText

        cols = len(encodedText) // rows # number of cols
        answer = []

        for i in range(cols) : # 0, 1
            for j in range(rows) : 
                idx = i + j*(cols+1) # Index of encodedText

                if idx >= len(encodedText) : # If out of index
                    break
                else : 
                    answer.append(encodedText[idx])

        return ''.join(answer).rstrip()

# ch   ie   pr (12, 3, 4)
# 123456789012
# 0 5 10, 1 6 11 => 6
# 0 1 2 , 3 4 5

# iveo    eed   l te   olc (15, 4, 3)
# 123456789012345678901234
# 1 8 15 22, 2 9 16 23, 3 10 17 24, 4 11 18 => 15