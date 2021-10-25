class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        del nums1[m:]
        i = 0
        j = 0 
        while(i < len(nums1) and j < n):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] == nums2[j]:
                nums1.insert(i+1, nums2[j])
                i += 2
                j += 1
            elif nums1[i] > nums2[j]:
                nums1.insert(i, nums2[j])
                i += 1
                j += 1
                
                
        for k in range(j, n):
            nums1.insert(i, nums2[k])
            i += 1
            