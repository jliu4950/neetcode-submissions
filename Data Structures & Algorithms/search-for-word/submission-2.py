class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])
        used = [[False] * m for _ in range(n)]

        def dfs(pos,x,y):
            #print(used)
            nonlocal res
            pos += 1
            if pos == len(word):
                res = True
                return
            
            for nx,ny in [[x - 1,y],[x + 1, y],[x, y - 1],[x, y + 1]]:
                    if 0 <= nx < n and 0 <= ny < m:
                        if board[nx][ny] == word[pos] and not used[nx][ny]:
                            #print(nx,ny)
                            used[nx][ny] = True
                            dfs(pos,nx,ny)
                            used[nx][ny] = False



        res = False
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    #print(i,j)
                    used[i][j] = True
                    dfs(0,i,j)
                    used[i][j] = False
        return res