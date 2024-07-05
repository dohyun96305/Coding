# Find the Minimum and Maximum Number of Nodes Between Critical Points
# https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/description/

# Given a linked list head, return an array [minDistance, maxDistance] representing the minimum and maximum distances between any two distinct critical points 
# (local maxima or minima), or [-1, -1] if there are fewer than two critical points.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """
        temp = [] # Store critical point's index

        k, head = head.val, head.next 
        count = 2
        
        if not head.next : # if length of head < 2 => No critical point
            return [-1, -1]

        else : 
            while head.next : 
                if (head.val > k and head.val > head.next.val) or (head.val < k and head.val < head.next.val) : # Condition of Critical Point
                    temp.append(count) 
                k, head = head.val, head.next

                count += 1

        if not temp or len(temp) == 1 : # If critical point < 2 => return [-1, -1]
            return [-1, -1]

        max_len = temp[-1] - temp[0] # Max dist of critical point
        min_len = max_len 

        for a, b in zip(temp[:-1], temp[1:]) : 
            min_len = min(min_len, b-a) # Min dist of critical point

        return [min_len, max_len]



