# Subsets
# https://leetcode.com/problems/subsets/description
# Given a unique integer array, return all possible subsets (the power set) without duplicates, in any order.

# Backtracking 

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        answer = []
        self.backtracking(nums, 0, [], answer)
        return answer

    def backtracking(self, nums, index, curr, answer) :  
        if index == len(nums) : 
            answer.append(curr[:])
            return 

        self.backtracking(nums, index+1, curr, answer)
        curr.append(nums[index])
        self.backtracking(nums, index+1, curr, answer)
        curr.pop()

solution = Solution()
print(solution.subsets([1, 2, 3]))