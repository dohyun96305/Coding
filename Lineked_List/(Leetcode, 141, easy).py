# https://leetcode.com/problems/linked-list-cycle/description/
# Linked List Cycle
# Linked LIst에 Cycle 여부 확인

# 토끼와 거북이 알고리즘
# 강의 참조
# https://www.youtube.com/watch?time_continue=280&v=RRSItF-Ts4Q&embeds_referring_euri=https%3A%2F%2Fleetcode.com%2F&source_ve_path=MjM4NTE&feature=emb_title
# https://velog.io/@lacomaco/%ED%86%A0%EB%81%BC%EC%99%80-%EA%B1%B0%EB%B6%81%EC%9D%B4-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-LeetCode-142
# (Leetcode, 287, medi 참고)

# Definition or singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        head1 = head # head, head1 pointer 생성
        
        while head1 and head1.next:
            head = head.next # slow pointer => 한번에 next 1번씩
            head1 = head1.next.next # fast pointer => 한번에 next 2번씩
            
            if head is head1:
                return True # slow와 fast가 같다면 cycle이 있다 => 처음 중복되는 지점이 순환점의 시작점
        
        return False
        

        
        