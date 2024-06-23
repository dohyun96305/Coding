# Minumum Increment to Make Array Unique
# https://leetcode.com/problems/minimum-increment-to-make-array-unique/description/?envType=daily-question&envId=2024-06-14
# Find the minimum number of increments needed to make all elements in an integer array unique.

class Solution(object):
    def minIncrementForUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums.sort()
        count = 0

        for i in range(1, len(nums)) : 
            if nums[i-1] >= nums[i] : 
                count += nums[i-1] - nums[i] + 1
                nums[i] = nums[i-1] + 1

        return count           

# 1 1 2 2 3 7
# 1 2 3 4 5 7