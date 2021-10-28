class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        n = len(board)
        
        for i in range(n):
            # collecting row elements in a list
            row = [board[i][j] for j in range(n) if board[i][j] != '.']
            # check if row has any elem twice
            if len(row) != len(set(row)):
                return False
            
            # collecting column element in a list
            col = [board[j][i] for j in range(n) if board[j][i] != '.']
            # check if column has any elem twice
            if len(col) != len(set(col)):
                return False
            
        # collect grid element and check if any grid has any elem twice
        for i in range(3):
            for j in range(3):
                grid = []
                for k in range(3):
                    for l in range(3):
                        if board[i*3+k][j*3+l] != '.':
                            grid.append(board[i*3+k][j*3+l])
                if len(grid) != len(set(grid)):
                    return False
        
        return True

