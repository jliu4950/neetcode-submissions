import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # 在所有路线中，找高点最低的那一条
        hp = [(grid[0][0],(0,0))]
        rows = len(grid)
        cols = len(grid[0])

        dst = (rows - 1,cols - 1)
        visited = set()
        visited.add((0,0))

        direction = [[0,-1],[0,1],[-1,0],[1,0]]

        while hp:
            h,(r,c) = heapq.heappop(hp)
            if (r,c) == dst:
                return h
            for x,y in direction:
                nr = r + x
                nc = c + y
                if 0 <= nr < rows and 0<= nc < cols and (nr,nc) not in visited:
                    nh = max(h,grid[nr][nc])
                    heapq.heappush(hp,(nh,(nr,nc)))
                    visited.add((nr,nc))

