class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        hashTable = {}
        n = len(nums1)
        n2 = len(nums2)
        result = [-1] * n
        temp = [-1] * n2
        
        # find the next greater element of elements in nums2 by single pass
        # store it to temp
        stack = []
        for j, num in enumerate(nums2):
            hashTable[num] = j
            while stack and nums2[stack[-1]] < num:
                temp[stack.pop()] = num
                
            stack.append(j)
                
        # now put next greater elemnt of nums2 in the result list for nums1[i] = nums2[j]
        for k in range(n):
            result[k] = temp[hashTable[nums1[k]]]
        
        return result