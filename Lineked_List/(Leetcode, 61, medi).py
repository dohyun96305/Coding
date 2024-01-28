# https://leetcode.com/problems/rotate-list/
# Rotate List
# Linked List rotate 한 후 결과 출력 

# Linked List
# ListNode{val: 1, 
#          next: ListNode{val: 2, 
#                         next: ListNode{val: 3, 
#                                        next: ListNode{val: 4, 
#                                                       next: ListNode{val: 5, 
#                                                                      next: None}}}}}

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not k : # 예외 처리
            return head

        head1 = head
        len1 = 1 # head len 확인 

        while head1.next : # head1.next를 통해 next: None 나올때 까지 len + 1
            len1 += 1
            head1 = head1.next

        head1.next = head # None에 head를 통해 cycle 형성 => 1, 2, 3, 4, 5, 1, 2, 3, ....

        # rotate 횟수 : left value move => k%len1, right value move => len1 - k%len1

        for _ in range(len1-(k%len1)) : 
            head1 = head1.next
        
        head = head1.next
        head1.next = None # None 지정을 통해 cycle 마무리

        return head
        
        