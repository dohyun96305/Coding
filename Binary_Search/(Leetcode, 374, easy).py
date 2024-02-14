# https://leetcode.com/problems/guess-number-higher-or-lower/description
# Guess Number Higher or Lower
# 숫자 맞추기 게임

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """

        start = 1
        end = n
        check = 1

        while check != 0 : 
            mid = (start + end) // 2
            check = guess(mid) # 미리 선언된 함수 guess 이용

            if check == 1 : 
                start = mid + 1 
            else : 
                end = mid - 1

        return mid
        