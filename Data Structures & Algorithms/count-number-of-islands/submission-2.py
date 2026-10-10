class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        visited = set()
        islands = 0
        # dfs
        def dfs(r,c):
            if grid[r][c] == "0" or (r,c) in visited:
                return
            
            directions = [[1,0],[-1,0],[0,1],[0,-1]]
            visited.add((r,c))

            for dr,dc in directions:
                nr = dr + r
                nc = dc + c
                if nr in range(row) and nc in range(col) and grid[nr][nc] == "1" and (nr,nc) not in visited:
                    dfs(nr,nc)
            
        #detect island
        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1" and (r,c) not in visited:
                    # print(r,c)
                    # print(visited)
                    dfs(r,c)
                    islands += 1
        return islands