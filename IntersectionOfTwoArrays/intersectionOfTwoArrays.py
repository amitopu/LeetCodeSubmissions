class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        # sort the arrays first
        nums1.sort()
        nums2.sort()
        
        # initialize two pointing variables to 0 so they point to beginning of the arrays
        # iterate through both the arrays and check the elements of index i j of subsequent arrays are equal
        # if equal append the elment to result array and increase i j by 1
        # if one array element is smaller than other increase that pointing variable by one
        i = 0
        j = 0
        new = []
        while(i < len(nums1) and j < len(nums2)):
            if nums1[i] == nums2[j]:
                new.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                i += 1
        return new