class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        digit=["0","1","2","3","4","5","6","7","8","9"]

        for i in range(9):
            seen=set()
            for j in range(9):
                if board[i][j] in seen:
                    return False
                if board[i][j] in digit:
                    seen.add(board[i][j])
        
        for j in range(9):
            seen=set()
            for i in range(9):
                if board[i][j] in seen:
                    return False
                if board[i][j] in digit:
                    seen.add(board[i][j])
        
        for row in range(3):
            for col in range(3):
                seen=set()
                for i in range(3):
                    for j in range(3):
                        r=i+3*row
                        c=j+3*col
                        if board[r][c] in seen:
                            return False
                        if board[r][c] in digit:
                            seen.add(board[r][c])
        
        return True
                
        