# Open the Lock
# https://leetcode.com/problems/open-the-lock/?envType=daily-question&envId=2024-07-06
# Determine the minimum number of moves to unlock a 4-wheel lock starting at "0000" to a given target code, avoiding any deadends where the lock freezes, or return -1 if the target is unreachable.

# BFS

from collections import deque

class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """

        if '0000' in deadends : # Exception
            return -1

        def turn_digit(num1) : # To make list available digit with 1 turn 
            temp = []

            for i in range(4): 
                k_plus = str((int(num1[i])+1) % 10) # with 1 plus turn
                k_minus = str((int(num1[i])-1) % 10) # with 1 minus turn

                num1_plus = num1[:i] + k_plus + num1[i+1:]
                num1_minus = num1[:i] + k_minus + num1[i+1:] 

                temp.append(num1_plus)
                temp.append(num1_minus)

            return temp

        temp = deque()
        temp.append(['0000', 0]) # BFS list
        deadends = set(deadends) # visited + limited digit

        while temp : 
            digit, turn = temp.popleft()

            if digit == target : 
                return turn 

            for a in turn_digit(digit) : 
                if a not in deadends :
                    deadends.add(a) # Plus visited digit
                    temp.append([a, turn+1])

        return -1