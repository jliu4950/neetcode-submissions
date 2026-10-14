class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        pac = set()
        atl = set()

        def dfs(r,c,visited,pre):
            if r not in range(rows) or c not in range(cols) or (r,c) in visited or heights[r][c] < pre:
                return 
            
            visited.add((r,c))
            dfs(r - 1,c,visited,heights[r][c])
            dfs(r + 1,c,visited,heights[r][c])
            dfs(r ,c - 1,visited,heights[r][c])
            dfs(r ,c + 1,visited,heights[r][c])

        for c in range(cols):
            dfs(0,c,pac,heights[0][c])
            dfs(rows - 1, c,atl ,heights[rows - 1][c])
        
        for r in range(rows):
            dfs(r,0,pac,heights[r][0])
            dfs(r,cols - 1,atl,heights[r][cols - 1])
        
        res = []
        # print(pac)
        # print(atl)
        for r,c in pac:
            if (r,c) in atl:
                res.append([r,c])
        
        return res