# https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/description/
# Find the Smallest Divisor Given a Threshold
# divisor 값으로 나눠 합 한 값이 Threshold 값에 작거나 같은 가장 큰 divosr 값 return

class Solution(object):

    def smallestDivisor(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        min1 = 1 # binary Search, left 값
        max1 = max(nums) # binary Search, right 값

        while min1 < max1 : # while 반복문 종료 조건 => left가 right보다 커질 때
            
            mid1 = (min1+max1) // 2 # # binary Search, mid 값
            sum1 = sum(-(-num // mid1) for num in nums) 
            # sum([(i/mid1) + 1 if i%mid1 != 0 else i/mid1 for i in nums])

            if sum1 > threshold : # sum1 값이 Threshold 값보다 크다면 더 큰 값으로 나눠야함
                min1 = mid1 + 1

            else : 
                max1 = mid1 # sum1 값이 Threshold 값보다 크다면 더 작은 값으로 나눠야함

        return min1



        
# divisor => divided all nums and sum
# closet sum to threshold 
# return smalles divisor
# 7/3 = 2.XX => 3
# 10/2 = 5 => 5