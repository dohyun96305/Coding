# https://leetcode.com/problems/container-with-most-water/description
# Container with Most Water
# 기둥의 높이가 주어진 리스트에서 가장 많이 저장할 수 있는 물의 용량 return

# Two-Pointers가 Binary-Search와 다른점 
# Two-Pointer : left, right 한 칸씩 이동하면서 탐색
# Binary-Search : left, right 사이 mid를 통해 탐색, 데이터가 정렬되어 있어야함. 

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        left = 0
        right = len(height) - 1
        water = 0 

        while left <= right : 
            distance = right - left # 너비, 두 기둥 사이 거리
            height1 = min(height[left], height[right]) # 높이, 두 기둥 중 짧은 기둥

            water = max(water, distance * height1) # 물 용량 = 너비 * 높이

            if height[left] >= height[right] :  # 기둥이 짧은 쪽이 이동 
                right -= 1

            else : 
                left += 1

        return water
        