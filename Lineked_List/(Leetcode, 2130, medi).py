# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/description
# Maximum Twin Sum of a Linked List
# Linked list, 양쪽 끝에서부터의 두 수의 합의 max 값


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        slow = head
        fast = head

        prev = None # 중간 위치에서 처음으로 거꾸로 오는 Linked List 생성
        answer = 0

        while fast : # 중간 위치 확인 (slow : 1칸씩, fast : 2칸씩 => fast가 끝에 도착한다면 slow는 중간에 위치)
            fast = fast.next.next
            slow.next, slow, prev = prev, slow.next, slow

            # slow.next = prev, slow = slow.next, prev = slow 
            # slow.next를 prev에 역순으로 저장 => prev 생성 
            # 기존 slow는 slow.next 진행

        while prev and slow : # prev : 중간에서 처음으로, slow : 중간에서 끝으로 
            answer = max(prev.val+slow.val, answer)
            prev = prev.next
            slow = slow.next
            
        return answer
   