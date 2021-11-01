# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # edge cases
        if l1 is None and l2 is None:
            return None
        elif l1 is None:
            return l2
        elif l2 is None:
            return l1
        
        
        point1 = l1
        point2 = l2
        prev = None
        while point1 is not None and point2 is not None:
            if point1.val < point2.val:
                prev = point1
                point1 = point1.next
            else:
                if prev is not None:
                    prev.next = point2
                prev = point2
                point2 = point2.next
                prev.next = point1
        
        # managing remaining nodes in the remaining node list
        if point1 is not None:
            prev.next = point1
        if point2 is not None:
            prev.next = point2
        
        # returning head which has lower vlaue
        if l1.val < l2.val:
            return l1
        else:
            return l2


# Another faster solution
# Needs less operation

# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
#         # initializing the result node and a pointer currentNode pointing to it
        
#         result = ListNode(0)
#         currentNode = result
        
#         # iterating over l1 and l2 and updating the result node
        
#         while l1 is not None and l2 is not None:
#             if l1.val < l2.val:
#                 currentNode.next = l1
#                 l1 = l1.next
#             else:
#                 currentNode.next = l2
#                 l2 = l2.next
                
#             # point the currentNode to latest node
#             currentNode = currentNode.next
        
#         # managing the rest of the nodes
        
#         if l1 is not None:
#             currentNode.next = l1
#         else:
#             currentNode.next = l2
        
#         return result.next