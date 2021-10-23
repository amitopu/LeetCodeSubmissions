class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # initialize local and gobal max to 0
        currentMax = nums[0]
        realMax = nums[0]
        # iterate through 1 to last element.
        # local max number is the max(local max + elem, elem) to ensure taking the higher number
        # update global max comparing with local max in each iteration
        # after all iteration the max sum of subarray will be the global max
        for i in range(1,len(nums)):
            currentMax = max(nums[i]+ currentMax, nums[i])
            if currentMax > realMax:
                realMax  = currentMax
        return realMax


# Second Solution

# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         currentMax = 0
#         realMax = nums[0]
#         for n in nums:
#             if currentMax < 0:
#                 currentMax = 0
#             currentMax = currentMax + n
#             if currentMax > realMax:
#                 realMax = currentMax
#         return realMax