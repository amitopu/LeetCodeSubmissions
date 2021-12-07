class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            leftnum = nums[left]
            rightnum  =nums[right]
            midnum = nums[mid]
            if target == midnum:
                return mid
            elif leftnum <= midnum:
                if target >= leftnum and target < midnum:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if target > midnum and target <= rightnum:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1