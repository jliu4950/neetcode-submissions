class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        max_area = 0
        island_area = 0

        def dfs(r,c):
            nonlocal island_area
            if grid[r][c] == 0:
                return
            
            island_area += 1
            visited.add((r,c))
            directions = [[-1,0],[1,0],[0,1],[0,-1]]

            for dr,dc in directions:
                nr = r + dr
                nc = c + dc
                if nr in range(rows) and nc in range(cols) and (nr,nc) not in visited and grid[nr][nc] == 1:
                    dfs(nr,nc)
            

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    dfs(r,c)
                    max_area = max(max_area,island_area)
                    island_area = 0
        
        return max_area