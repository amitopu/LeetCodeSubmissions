# first solution 
# Space complexity O(1)
# Time Complexity O(n)

class Solution:
    def sortColors(self, nums: list[int]) -> None:
        left = 0
        for elem in [0,1]:
            for i in range(left, len(nums)):
                if nums[i] == elem:
                    nums[left], nums[i] = nums[i], nums[left]
                    left += 1

