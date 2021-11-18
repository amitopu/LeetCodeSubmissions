class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # O(n) time | O(n) space
        stack = []
        n = len(nums)
        result = [-1] * n
        
        for i in range(n):
            num = nums[i]
            while stack and nums[stack[-1]] < num:
                result[stack.pop()] = num
                
            stack.append(i)
        
        for i in range(n):
            num = nums[i]
            while stack and nums[stack[-1]] < num:
                result[stack.pop()] = num
                
        
        
        return result 
            