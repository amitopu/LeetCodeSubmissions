# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        # this is naive recursive solution


        result = []
        self.traversal(root, result)
        return result
    
    def traversal(self, root, result):
        if not root:
            return
        self.traversal(root.left, result)
        result.append(root.val)
        self.traversal(root.right, result)


# another solution which is iterative

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []
        while root:
            if root.right:
                tmp = root.right
                root.right = None
                stack.append(tmp)
            if root.left:
                temp = root.left
                root.left = None
                stack.append(root)
                root = temp
            else:
                result.append(root.val)
                if len(stack) == 0:
                    break
                root = stack.pop()
        
        return result