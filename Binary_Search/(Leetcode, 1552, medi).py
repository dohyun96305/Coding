# Magnetic Force Between Two Balls
# https://leetcode.com/problems/magnetic-force-between-two-balls/description
# Given an array position of basket locations and m balls, 
# distribute the balls into the baskets such that the minimum magnetic force (|x - y|) between any two balls is maximized, and return that maximum possible force.

class Solution(object):
    def check(self, position, m, num1) : 
        prev = position[0]
        count = 1

        for i in range(1, len(position)) : 
            if position[i] - prev >= num1 : 
                prev = position[i]
                count += 1
            
            if count == m : 
                return True
            
        return False

    def maxDistance(self, position, m):
        """
        :type position: List[int]
        :type m: int
        :rtype: int
        """
        position.sort()
        answer = 0

        left, right = 1, (position[-1] - position[0])

        while left <= right : 
            mid = (left + right) // 2

            if self.check(position, m, mid) : 
                answer = mid
                left = mid + 1
            else : 
                right = mid - 1

        return answer

answer = Solution()
print(answer.maxDistance([1,2,3,4,7], 3))