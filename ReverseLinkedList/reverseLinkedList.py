# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # managing edge case
        if head is None:
            return None
        
        current = head
        newHead = None
        
        while head is not None:
            head = head.next
            current.next = newHead
            newHead = current
            current = head
        
        return newHead