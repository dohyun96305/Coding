# Magic Squares In Grid
# https://leetcode.com/problems/magic-squares-in-grid/description
# Given a grid of integers
# the task is to count how many 3x3 contiguous subgrids are magic squares, where each row, column, and diagonal sums to the same value, and the square contains distinct numbers from 1 to 9.

class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def check(x, y) :
            num_check = [False] * 10 # num_check
            sum_row = [0] * 3       # row_sum
            sum_col = [0] * 3       # col_sum
            diag_1, diag_2 = 0, 0   # diag_check
            
            for i in range(3) : # x
                for j in range(3) : # y
                    if grid[x+i][y+j] < 1 or grid[x+i][y+j] > 9 : # num_check
                        return False

                    if num_check[grid[x+i][y+j]] == True : # num_check
                        return False

                    num_check[grid[x+i][y+j]] = True # num_check
                    sum_row[i] += grid[x+i][y+j]  # row_sum
                    sum_col[j] += grid[x+i][y+j]  # col_sum

                diag_1 += grid[x+i][y+i]
                diag_2 += grid[x+2-i][y+2-i]

            for i in range(3) : 
                if sum_row[i] != 15 or sum_col[i] != 15 : 
                    return False
                
            if diag_1 != 15 or diag_2 != 15 : 
                return False

            return True

        x, y = len(grid), len(grid[0]) # Row, Column
        answer = 0
        
        if x < 3 or y < 3 : # If no Square => Return False
            return 0

        for i in range(0, x-2) : 
            for j in range(0, y-2) : 
                if check(i, j) : # If Magic_square => += 1
                    answer += 1

        return answer