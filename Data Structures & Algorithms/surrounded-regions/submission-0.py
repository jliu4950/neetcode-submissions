class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])
        visited = set()
        
        def dfs(r,c):
            if r not in range(ROWS) or c not in range(COLS) or (r,c) in visited or board[r][c] == "X":
                return 
            
            visited.add((r,c))
            board[r][c] = 'T'
            dfs(r - 1,c)
            dfs(r + 1,c)
            dfs(r,c - 1)
            dfs(r,c + 1)

        for c in range(COLS):
            if board[0][c] == "O" and (0,c) not in visited:
                dfs(0,c)
            if board[ROWS - 1][c] == "O" and (ROWS - 1,c) not in visited:
                dfs(ROWS - 1 ,c)
        
        for r in range(ROWS):
            if board[r][0] == "O" and (r,0) not in visited:
                dfs(r,0)
            if board[r][COLS -1] == "O" and (r,COLS - 1) not in visited:
                dfs(r,COLS - 1)

        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"