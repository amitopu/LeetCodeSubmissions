class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        # iterative solution


        ans = []
        if root is None:
            return ans
        stack = []
        while(root):
            if root.right:
                stack.append(root.right)
            ans.append(root.val)
            root = root.left
            if root is None:
                if len(stack) == 0:
                    break
                root = stack.pop()
        return ans


# another recursive solution which is naive

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        self.traverse(root, ans)
        return ans
        
    def traverse(self, root, ans):
        if not root:
            return
        ans.append(root.val)
        self.traverse(root.left, ans)
        self.traverse(root.right, ans)