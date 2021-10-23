class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currentMax = nums[0]
        realMax = nums[0]
        for i in range(1,len(nums)):
            currentMax = max(nums[i]+ currentMax, nums[i])
            if currentMax > realMax:
                realMax  = currentMax
        return realMax