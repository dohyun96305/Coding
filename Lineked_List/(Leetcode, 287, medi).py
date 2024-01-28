# https://leetcode.com/problems/find-the-duplicate-number/description/
# Find the Duplicate Number
# List내 딱 한 개의 중복된 값 찾기

# 토끼와 거북이 알고리즘
# 강의 참조
# https://www.youtube.com/watch?time_continue=280&v=RRSItF-Ts4Q&embeds_referring_euri=https%3A%2F%2Fleetcode.com%2F&source_ve_path=MjM4NTE&feature=emb_title
# https://velog.io/@lacomaco/%ED%86%A0%EB%81%BC%EC%99%80-%EA%B1%B0%EB%B6%81%EC%9D%B4-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-LeetCode-142
# (Leetcode, 141, easy 참고)

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        slow = nums[0] 
        fast = nums[nums[0]]

        while True: # cycle 확인
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break
    
    # 중복되는 숫자 확인 (순환 루프 시작점 확인) 
    # slow == fast 지점에서 slow를 0으로 옮김 => 이후 만나는 지점이 중복되는 숫자 (루프 시작점) 
    # 첨부된 2번째 링크 확인 + 수식 확인
    #   => (시작점 - 순환 루프 시작점) 거리와 (slow == fast - 순환 루프 시작점) 거리가 같음을 확인
    
        slow = 0 # 시작점 초기화 

        while slow != fast : 
            slow = nums[slow]
            fast = nums[fast]
            
        return slow