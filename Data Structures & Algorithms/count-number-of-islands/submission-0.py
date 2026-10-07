class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        direction = [[1,0],[-1,0],[0,1],[0,-1]]
        m = len(grid)
        n = len(grid[0])
        visited = [[False] * n for _ in range(m)]
        cnt = 0

        def dfs(x,y):
            #print(x,y)
            if grid[x][y] == "0" or visited[x][y]:
                return
            visited[x][y] =  True
            for i,j in direction:
                nx = x + i
                ny = y + j
                if 0 <= nx <len(grid) and 0<= ny < len(grid[0]):
                    dfs(nx,ny)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and not visited[i][j]:
                    dfs(i,j)
                    cnt += 1

        return cnt      