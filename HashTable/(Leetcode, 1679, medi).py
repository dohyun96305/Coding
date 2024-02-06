# https://leetcode.com/problems/max-number-of-k-sum-pairs/description
# Max Number of K-Sum Pairs
# hashtable 문제, 두 숫자의 합이 k를 만족하는 쌍의 개수

# 쌍의 개수를 구하는 문제 => 주어진 nums 안에 중복된 숫자의 개수를 잘 컨트롤 하는 것이 핵심

class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        hash = {} # hashtable 생성 
        answer = 0 

        for i in nums : 
            diff = k - i 

            if diff in hash and hash[diff] > 0 : # 쌍이 존재할 경우
                answer += 1
                hash[diff] -= 1 # 차이값의 개수 -1
                                # i는 hash에 저장하지 않는다 ( 개수 -1 )

            elif i in hash : 
                hash[i] += 1 # hash에 존재할 경우 += 1

            else : 
                hash[i] = 1 # hash에 존재하지 않을 경우 1 초기화
            

        return answer