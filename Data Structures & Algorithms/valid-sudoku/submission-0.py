class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #row
        for i in board:
            h1 = {}
            for j in i:
                if j in h1 and j!=".":
                    h1[j] += 1
                    return False
                else:
                    h1[j] = 1
        
        #column
        for i in range(9):
            h2 = {}
            for j in board:
                if j[i] in h2 and j[i]!=".":
                    h2[j[i]] += 1
                    return False
                else:
                    h2[j[i]] =1
                
        #box
        for k in range(0,9,3):
            for l in range(0,9,3):
                h3 = {}
                for i in range(k,k+3):
                    for j in range(l, l+3):
                        if board[i][j] in h3 and board[i][j] != ".":
                            h3[board[i][j]] += 1
                            return False
                        else:
                            h3[board[i][j]] = 1
        
        return True
        