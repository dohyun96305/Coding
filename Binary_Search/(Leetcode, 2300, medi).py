# https://leetcode.com/problems/successful-pairs-of-spells-and-potions/description
# Successful Pairs of Spells and Potions
# success 이상 spell *[potions] 내 potions 개수 return

class Solution(object):
    def successfulPairs(self, spells, potions, success):
        """
        :type spells: List[int]
        :type potions: List[int]
        :type success: int
        :rtype: List[int]
        """

        answer = [0] * len(spells) # answer return
        potions.sort() # binary_search를 위한 sort()
        count = 0 # answer 위치를 위한 count

        for i in spells : 
            start = 0 
            end = len(potions) - 1

            while start <= end : 
                mid = (start+end) // 2
                num = potions[mid] * i # target 값 => spell * potions[mid]

                if num >= success : 
                    end = mid - 1
                else : 
                    start = mid + 1
                
            target = len(potions) - start # start 위치 => 조건 만족하는 가장 최솟값 위치
            answer[count] = target
            
            count += 1 

        return answer