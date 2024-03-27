# https://leetcode.com/problems/reverse-linked-list/description
# Reversed Linked List
# 주어진 Linked List를 역순으로 출력

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        prev = None 

        while head : 
            head.next, prev, head = prev, head, head.next
            
        return prev
        