class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        import math
        arr = []
        for i in range(rowIndex + 1):
            arr.append(math.comb(rowIndex, i))
        return arr
        
        