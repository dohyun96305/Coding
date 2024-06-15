# Remove Duplicates from Sorted List
# https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/
# Linked_List
# 중복된 val 제거된 후 List return 

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        current = head # pointer 생성 
        
        while current and current.next : 
            if current.val == current.next.val : 
                current.next = current.next.next

            else :
                current = current.next

        return head
        