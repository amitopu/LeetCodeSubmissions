class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        arr = []
        temp = []
        count = 0
        # iterate for rows
        for i in range(numRows):
            # iterate for columns
            for j in range(i+1):
                # if it is the first element in the current row, apend 1
                if j == 0:
                    count += 1
                    temp.append(1)
                    
                # if it is the last element in the current row, append 1
                elif j == i and j != 0:
                    count += 1
                    temp.append(1)
                
                # if it is not the first or last element then calculate it and append
                elif j != 0:
                    count += 1
                    # current element is sum of two elements top of it
                    temp.append(arr[i-1][j-1] + arr[i-1][j])
                    
                # append the row in the outer array if column number is reached to limit
                if count == i + 1:
                    arr.append(temp)
                    temp = []
                    count = 0
                    
        return arr



### different solution



# class Solution:
#     def generate(self, numRows: int) -> List[List[int]]:
#         new = []
        
#         new.append([1])
        
#         if numRows > 1:
#             new.append([1,1])
#         else:
#             return new
        
#         for i in range(2, numRows):
#             prev_row = new[-1]
#             prev = 0
#             temp = []
#             for v in prev_row:
#                 temp.append(v + prev)
#                 prev = v
#             temp.append(1)
#             new.append(temp)
        
#         return new