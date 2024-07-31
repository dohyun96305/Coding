# Boats to Save People
# https://leetcode.com/problems/boats-to-save-people/description
# Return the minimum number of boats needed to carry all people, given that each boat can carry at most two people whose combined weight does not exceed a specified limit.

##### Each boat carries at most two people at the same time 

class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()

        left, right = 0, len(people) - 1 # Two-Pointers
        answer = 0

        while left <= right : 
            if people[left] + people[right] <= limit : # Contains Two people maximum
                left += 1 # Boat can contain people[left]

            right -= 1 # Boat contain people[right]
            answer += 1 # Boat count => answer
        
        return answer

        