# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # O(log(n)) avg time and O(1) avg space | O(n) worst time and O(1) worst space
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        currentNode = root
        while currentNode:
            if val == currentNode.val:
                return currentNode
            elif val > currentNode.val:
                currentNode = currentNode.right
            elif val < currentNode.val:
                currentNode = currentNode.left
        
        return None
        

