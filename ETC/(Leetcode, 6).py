# https://leetcode.com/problems/zigzag-conversion/description/
# ZigZag_Conversion 
# numRows 값에 따라 문자열 S를 지그재그로 변환 및 반환

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        temp = [''] * numRows # numRows 값에 따라 빈 문자열 및 List 생성 

        index = 0

        if numRows == 1 or numRows >= len(s) : 
            return s

        else : 
            for i in s : # Time Complexity : O(n)
                up = 1
                down = -1
                temp[index] += i # numRows 및 Index에 따라 temp List에 문자열 하나씩 저장

                if index == 0 : # 0 ~ numRows-1 까지는 1씩 증가
                    move = up
                elif index == numRows -1 : # numRows-1 ~ 0까지는 1씩 감소
                    move = down

                index = index + move # Index 값에 따른 move 증가

            return ''.join(temp) # 조건문 완료 후 temp 내 문자열 붙여서 반환
                

# ((3))
# 0 1 2 3 4 5 6 7 8
# 0 1 2 1 0 1 2 1 0

# ((4))
# 0 1 2 3 4 5 6 7 8 9 10 11 12
# 0 1 2 3 2 1 0 1 2 3 2  1  0