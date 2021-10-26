class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        # if reshaping is not possible return the original matrix
        
        if type(mat[0]) is list: # check if the input martix is 2d
            if c * r != len(mat) * len(mat[0]):
                return mat
            else:
                mat2 = []
                temp = []
                count = 0
                for i in range(len(mat)):
                    for j in range(len(mat[0])):
                        temp.append(mat[i][j])
                        count += 1
                        if count == c:
                            mat2.append(temp)
                            temp = []
                            count = 0
                return mat2
                
        else:
            # if the input matrix is 1d
            if len(mat) != c * r:
                return mat
            else:
                mat2 = []
                temp = []
                count = 0
                for i in range(len(mat)):
                    for j in range(len(mat[0])):
                        temp.append(mat[i][j])
                        count += 1
                        if count == c:
                            mat2.append(temp)
                            temp = []
                            count = 0
                return mat2
                