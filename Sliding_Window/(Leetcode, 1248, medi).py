# Count Number of Nice Subarrays
# https://leetcode.com/problems/count-number-of-nice-subarrays/description
# Return the count of continuous subarrays in nums containing exactly k odd numbers.

class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        temp_list = [0] * (len(nums) + 1) 
        temp_list[0] = 1

        answer = 0
        temp = 0 

        for i in nums : 
            temp += i % 2                       # Check whether is odd number 

            if temp - k >= 0 :                  # If enough odd number in subarrays 
                answer += temp_list[temp - k]

            temp_list[temp] += 1

        return answer

answer = Solution()
print(answer.numberOfSubarrays([1,1,2,1,1], 3))