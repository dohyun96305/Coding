# https://leetcode.com/problems/two-sum/description/
# ZigZag_Conversion 
# List 내 2개 원소의 합이 Target 값이라면 Index 값 반환

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        temp = {} # HashTable 생성, 값 : Index 저장

        for i, k in enumerate(nums) : # Time Complexity : O(n)
            
            diff = target - k # 반복문을 통해 조건 확인

            if diff in temp : # 조건을 만족하는 값이 HashTable에 있다면 Index 값 반환
                return [temp[diff], i]

            temp[k] = i # 조건을 만족하지 못한다면 HashTable 값 저장 


            
        