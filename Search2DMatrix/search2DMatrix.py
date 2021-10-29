class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # Perform binary search to check if a target is in the range of numbers in a row
        # Perform binary search in that row to check if target is found

        row_count = len(matrix)
        col_count = len(matrix[0])
        left = 0
        right = row_count
        mid = row_count // 2

        while(left < right):
            if target >= matrix[mid][0] and target <= matrix[mid][col_count-1]:
                return self.binarySearch(matrix[mid], target)
            
            elif target < matrix[mid][0]:
                right = mid
                mid = left + (right - left) // 2
            
            elif target > matrix[mid][0]:
                left = mid + 1
                mid = left + (right - left) // 2
                
    def binarySearch(self, arr, target):
        n = len(arr)
        r = n
        l = 0
        m = n // 2
        
        while(l < r):
            if target ==  arr[m]:
                return True
            
            elif target > arr[m]:
                l = m + 1
                m = l + (r - l) // 2
            elif target < arr[m]:
                r = m
                m = l + (m - l) // 2
                
        return False